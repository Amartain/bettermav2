drop table jegyek;
drop table felhasznalok;
drop table menetrendek;
drop table megallok;
drop table vonatvonalak;
drop table allomasok;
drop table varosok;


-- Városok tábla
CREATE TABLE Varosok (
    irsz NUMBER(5) PRIMARY KEY,
    nev VARCHAR2(255),
    regio VARCHAR2(255),
    orszag VARCHAR2(255)
);

-- Állomások tábla
CREATE TABLE Allomasok (
    id NUMBER PRIMARY KEY,
    varos_irsz NUMBER REFERENCES Varosok(irsz) ON DELETE SET NULL,
    nev VARCHAR2(255),
    cim VARCHAR2(255)
);

-- Vonalak tábla
CREATE TABLE VonatVonalak (
    id NUMBER PRIMARY KEY,
    nev VARCHAR2(255),
    honnan_id NUMBER REFERENCES Allomasok(id) ON DELETE CASCADE,
    hova_id NUMBER REFERENCES Allomasok(id) ON DELETE CASCADE
);

-- Megállók tábla
CREATE TABLE Megallok (
    id NUMBER PRIMARY KEY,
    vonal_id NUMBER REFERENCES VonatVonalak(id) ON DELETE CASCADE,
    nev VARCHAR2(255),
    elozo_id NUMBER REFERENCES Allomasok(id) ON DELETE SET NULL,
    kovetkezo_id NUMBER REFERENCES Allomasok(id) ON DELETE CASCADE,
    tav_kezdotol NUMBER,
    cim VARCHAR2(255) NOT NULL,
    menetrendek_id NUMBER
);

-- Menetrendek tábla
CREATE TABLE Menetrendek (
    id NUMBER PRIMARY KEY,
    megallo_id NUMBER REFERENCES Megallok(id) ON DELETE CASCADE,
    irany number(1) NOT NULL,
    indul TIMESTAMP,
    erkezik_kovetkezo TIMESTAMP,
    peron VARCHAR2(255)
);

-- Felhasználók tábla
CREATE TABLE Felhasznalok (
    email VARCHAR2(255) PRIMARY KEY,
    nev VARCHAR2(255),
    jelszo VARCHAR2(255),
    utastipus VARCHAR2(255),
    regisztracio_datuma DATE
);

-- Jegyek tábla
CREATE TABLE Jegyek (
    id NUMBER PRIMARY KEY,
    vonal_id NUMBER REFERENCES VonatVonalak(id) ON DELETE SET NULL,
    honnan_id NUMBER REFERENCES Allomasok(id) ON DELETE SET NULL,
    hova_id NUMBER REFERENCES Allomasok(id) ON DELETE SET NULL,
    felhasznalo_id VARCHAR2(255) REFERENCES Felhasznalok(email) ON DELETE CASCADE,
    ar NUMBER,
    tav NUMBER,
    ervenyesseg_kezdete DATE,
    ervenyesseg_vege DATE,
    vasarlas_ideje DATE,
    utastipus VARCHAR2(255)
);

-- Triggerek
-- Triggerek az Allomasok táblához
CREATE OR REPLACE TRIGGER trg_allomasok_delete
BEFORE DELETE ON Allomasok
FOR EACH ROW
BEGIN
    UPDATE Megallok SET elozo_id = NULL WHERE elozo_id = :OLD.id;
    UPDATE Megallok SET kovetkezo_id = NULL WHERE kovetkezo_id = :OLD.id;
    UPDATE VonatVonalak SET honnan_id = NULL WHERE honnan_id = :OLD.id;
    UPDATE VonatVonalak SET hova_id = NULL WHERE hova_id = :OLD.id;
END;
/

-- Triggerek a Megallok táblához
CREATE OR REPLACE TRIGGER trg_megallok_delete
BEFORE DELETE ON Allomasok
FOR EACH ROW
BEGIN
    UPDATE Megallok SET elozo_id = NULL WHERE elozo_id = :OLD.id;
    UPDATE Megallok SET kovetkezo_id = NULL WHERE kovetkezo_id = :OLD.id;
END;
/

CREATE OR REPLACE TRIGGER trg_mgll_delete_mntrnd
BEFORE DELETE ON Menetrendek
FOR EACH ROW
BEGIN
    UPDATE Megallok SET menetrendek_id = NULL WHERE menetrendek_id = :OLD.id;
END;
/

--Trigger a Jegyek táblához
CREATE OR REPLACE TRIGGER trg_jegy_vasarlas_ideje
BEFORE INSERT ON Jegyek
FOR EACH ROW
BEGIN
    :NEW.vasarlas_ideje := SYSDATE;
END;
/

--Trigger a Felhasznalo táblához
CREATE OR REPLACE TRIGGER trg_regisztacio_datuma
BEFORE INSERT ON Felhasznalok
FOR EACH ROW
BEGIN
    :NEW.regisztracio_datuma := SYSDATE;
END;
/

-- Pelda adatok
-- Varosok adat
INSERT INTO Varosok (irsz, nev, regio, orszag) VALUES (1, 'Budapest', 'Közép-Magyarország', 'Magyarország');
INSERT INTO Varosok (irsz, nev, regio, orszag) VALUES (2, 'Debrecen', 'Észak-Alföld', 'Magyarország');
INSERT INTO Varosok (irsz, nev, regio, orszag) VALUES (3, 'Szeged', 'Dél-Alföld', 'Magyarország');
INSERT INTO Varosok (irsz, nev, regio, orszag) VALUES (4, 'Békéscsaba', 'Dél-Alföld', 'Magyarország');
INSERT INTO Varosok (irsz, nev, regio, orszag) VALUES (5, 'Siófok', 'Dél-Dunántúl', 'Magyarország');
INSERT INTO Varosok (irsz, nev, regio, orszag) VALUES (6, 'Gyula', 'Dél-Alföld', 'Magyarország');
INSERT INTO Varosok (irsz, nev, regio, orszag) VALUES (7, 'Orosháza', 'Dél-Alföld', 'Magyarország');
INSERT INTO Varosok (irsz, nev, regio, orszag) VALUES (8, 'Székkutas', 'Dél-Alföld', 'Magyarország');
INSERT INTO Varosok (irsz, nev, regio, orszag) VALUES (9, 'Szentes', 'Kelet-Alföld', 'Magyarország');
INSERT INTO Varosok (irsz, nev, regio, orszag) VALUES (10, 'Hódmezővásárhely', 'Dél-Alföld', 'Magyarország');
INSERT INTO Varosok (irsz, nev, regio, orszag) VALUES (11, 'Kiskunfélegyháza', 'Dél-Alföld', 'Magyarország');
INSERT INTO Varosok (irsz, nev, regio, orszag) VALUES (12, 'Szolnok', 'Észak-Alföld', 'Magyarország');
INSERT INTO Varosok (irsz, nev, regio, orszag) VALUES (13, 'Kecskemét', 'Dél-Alföld', 'Magyarország');
INSERT INTO Varosok (irsz, nev, regio, orszag) VALUES (14, 'Mezőberény', 'Dél-Alföld', 'Magyarország');
INSERT INTO Varosok (irsz, nev, regio, orszag) VALUES (15, 'Balatonfüred', 'Dél-Dunántúl', 'Magyarország');
INSERT INTO Varosok (irsz, nev, regio, orszag) VALUES (16, 'Tatabánya', 'Közép-Dunántúl', 'Magyarország');
INSERT INTO Varosok (irsz, nev, regio, orszag) VALUES (17, 'Püspökladány', 'Észak-Alföld', 'Magyarország');
INSERT INTO Varosok (irsz, nev, regio, orszag) VALUES (18, 'Kiskunmajsa', 'Dél-Alföld', 'Magyarország');
INSERT INTO Varosok (irsz, nev, regio, orszag) VALUES (19, 'Mezőtúr', 'Észak-Alföld', 'Magyarország');
INSERT INTO Varosok (irsz, nev, regio, orszag) VALUES (20, 'Fonyód', 'Dél-Dunántúl', 'Magyarország');
INSERT INTO Varosok (irsz, nev, regio, orszag) VALUES (21, 'Sopron', 'Nyugat-Dunántúl', 'Magyarország');

-- Allomasok
INSERT INTO Allomasok (id, varos_irsz, nev, cim) VALUES (1, 1, 'Keleti Pályaudvar', 'Budapest, Baross tér');
INSERT INTO Allomasok (id, varos_irsz, nev, cim) VALUES (2, 1, 'Nyugati Pályaudvar', 'Budapest, Teréz krt');
INSERT INTO Allomasok (id, varos_irsz, nev, cim) VALUES (3, 1, 'Déli Pályaudvar', 'Budapest, Krisztina krt');
INSERT INTO Allomasok (id, varos_irsz, nev, cim) VALUES (4, 2, 'Vasútállomás', 'Debrecen, Petőfi tér');
INSERT INTO Allomasok (id, varos_irsz, nev, cim) VALUES (5, 2, 'Csapókert', 'Debrecen, Keresszegi utca');
INSERT INTO Allomasok (id, varos_irsz, nev, cim) VALUES (6, 3, 'Vasútállomás', 'Szeged, Indóház tér');
INSERT INTO Allomasok (id, varos_irsz, nev, cim) VALUES (7, 3, 'Rókus vasútállomás', 'Szeged, Pulz utca');
INSERT INTO Allomasok (id, varos_irsz, nev, cim) VALUES (8, 4, 'Vasútállomás', 'Békéscsaba, Andrássy út');
INSERT INTO Allomasok (id, varos_irsz, nev, cim) VALUES (9, 5, 'Vasútállomás', 'Siófok, Millennium park');
INSERT INTO Allomasok (id, varos_irsz, nev, cim) VALUES (10,6, 'Vasútállomás', 'Gyula, Halácsy utca');
INSERT INTO Allomasok (id, varos_irsz, nev, cim) VALUES (11,6, 'Vasútállomás', 'Gyula, Halácsy utca');
INSERT INTO Allomasok (id, varos_irsz, nev, cim) VALUES (12, 7, 'Vasútállomás', 'Orosháza, Állomás utca');
INSERT INTO Allomasok (id, varos_irsz, nev, cim) VALUES (13, 7, 'Orosházi tanyák', 'Orosháza, Bakó József krt');
INSERT INTO Allomasok (id, varos_irsz, nev, cim) VALUES (14, 8, 'Vasútállomás', 'Székkutas, Krisztina krt');
INSERT INTO Allomasok (id, varos_irsz, nev, cim) VALUES (15, 9, 'Vasútállomás', 'Szentes, Baross út');
INSERT INTO Allomasok (id, varos_irsz, nev, cim) VALUES (16, 10, 'Vasútállomás', 'Hódmezővásárhely, Kistópart utca');
INSERT INTO Allomasok (id, varos_irsz, nev, cim) VALUES (17, 10, 'Népkert', 'Hódmezővásárhely, Kisállomás sor');
INSERT INTO Allomasok (id, varos_irsz, nev, cim) VALUES (18, 11, 'Vasútállomás', 'Kiskunfélegyháza, Kossuth Lajos utca');
INSERT INTO Allomasok (id, varos_irsz, nev, cim) VALUES (19, 11, 'Városi park', 'Kiskunfélegyháza, Csanyi út');
INSERT INTO Allomasok (id, varos_irsz, nev, cim) VALUES (20, 12, 'Vasútállomás', 'Szolnok, Jubileumi tér');
INSERT INTO Allomasok (id, varos_irsz, nev, cim) VALUES (21, 13, 'Vasútállomás', 'Kecskemét, Kodály Zoltán tér');
INSERT INTO Allomasok (id, varos_irsz, nev, cim) VALUES (22, 13, 'Katonatelep', 'Kecskemét');
INSERT INTO Allomasok (id, varos_irsz, nev, cim) VALUES (23, 14, 'Vasútállomás', 'Mezőberény, Vasút utca');
INSERT INTO Allomasok (id, varos_irsz, nev, cim) VALUES (24, 15, 'Vasútállomás', 'Balatonfüred, Castricum tér');
INSERT INTO Allomasok (id, varos_irsz, nev, cim) VALUES (25, 16, 'Vasútállomás', 'Tatabánya, Jedlik Ányos utca');
INSERT INTO Allomasok (id, varos_irsz, nev, cim) VALUES (26, 17, 'Vasútállomás', 'Püspökladány, Vasút u. 1');
INSERT INTO Allomasok (id, varos_irsz, nev, cim) VALUES (27, 18, 'Vasútállomás', 'Kiskunmajsa, Csontos Károly utca');
INSERT INTO Allomasok (id, varos_irsz, nev, cim) VALUES (28, 19, 'Vasútállomás', 'Mezőtúr');
INSERT INTO Allomasok (id, varos_irsz, nev, cim) VALUES (29, 20, 'Vasútállomás', 'Fonyód, Ady Endre utca');
INSERT INTO Allomasok (id, varos_irsz, nev, cim) VALUES (30, 21, 'Vasútállomás', 'Sopron, Állomás utca');

--  VonatVonalak
INSERT INTO VonatVonalak (id, nev, honnan_id, hova_id) VALUES (1, 'InterCity', 1, 2);
INSERT INTO VonatVonalak (id, nev, honnan_id, hova_id) VALUES (2, 'Gyorsvonat', 2, 3);

-- Megallok
INSERT INTO Megallok (id, vonal_id, nev, elozo_id, kovetkezo_id, tav_kezdotol, cim, menetrendek_id) VALUES (1, 1, 'Kőbánya-Kispest', 1, 2, 1, 'Budapest', NULL);
INSERT INTO Megallok (id, vonal_id, nev, elozo_id, kovetkezo_id, tav_kezdotol, cim, menetrendek_id) VALUES (2, 1, 'Ferihegy', 2, 3, 10, 'Budapest', NULL);

--  Menetrendek
-- 0 normal irany, 1 vissz irany
INSERT INTO Menetrendek (id, megallo_id, irany, indul, erkezik_kovetkezo, peron) VALUES (1, 1, 0, TO_TIMESTAMP('08:00:00', 'HH24:MI:SS'), TO_TIMESTAMP('08:15:00', 'HH24:MI:SS'), '5a');
INSERT INTO Menetrendek (id, megallo_id, irany, indul, erkezik_kovetkezo, peron) VALUES (2, 2, 1, TO_TIMESTAMP('09:00:00', 'HH24:MI:SS'), TO_TIMESTAMP('09:20:00', 'HH24:MI:SS'), '2b');


-- Felhasznalok
INSERT INTO Felhasznalok (email, nev, jelszo, utastipus) VALUES ('janos@example.com', 'Kovács János', 'majdhashelve', 'student');
INSERT INTO Felhasznalok (email, nev, jelszo, utastipus) VALUES ('erika@example.com', 'Nagy Erika', 'majdHASH', 'senior');

-- Jegyek
INSERT INTO Jegyek (id, vonal_id, honnan_id, hova_id, felhasznalo_id, ar, tav, ervenyesseg_kezdete, ervenyesseg_vege, utastipus) VALUES (1, 1, 1, 2, 'janos@example.com', 3000, 195, TO_DATE('2024-04-01', 'YYYY-MM-DD'), TO_DATE('2024-04-30', 'YYYY-MM-DD'), 'student');
INSERT INTO Jegyek (id, vonal_id, honnan_id, hova_id, felhasznalo_id, ar, tav, ervenyesseg_kezdete, ervenyesseg_vege, utastipus) VALUES (2, 2, 2, 3, 'erika@example.com', 2500, 150, TO_DATE('2024-05-01', 'YYYY-MM-DD'), TO_DATE('2024-05-31', 'YYYY-MM-DD'), 'senior');

-- összes rekordok száma:
SET SERVEROUTPUT ON
DECLARE
    v_record_count NUMBER;
BEGIN
    
    SELECT 
        (SELECT COUNT(*) FROM Varosok) +
        (SELECT COUNT(*) FROM Allomasok) +
        (SELECT COUNT(*) FROM VonatVonalak) +
        (SELECT COUNT(*) FROM Megallok) +
        (SELECT COUNT(*) FROM Menetrendek) +
        (SELECT COUNT(*) FROM Felhasznalok) +
        (SELECT COUNT(*) FROM Jegyek)
    INTO v_record_count
    FROM dual;

    DBMS_OUTPUT.PUT_LINE('Az összes rekordok száma: ' || v_record_count);
END;
/

--Összetett lekérdezések
--Melyik felhasználó hány jegyet vett az adott állomásról indulva
SELECT f.email, a.nev, COUNT(*) FROM Felhasznalok f JOIN Jegyek J on f.email = J.felhasznalo_id JOIN Allomasok a ON J.honnan_id = a.id GROUP BY f.email, a.nev;

--Melyik állomásról hány jegyet vettek
SELECT a.nev as allomas, COUNT(*) as darab FROM Allomasok a JOIN Jegyek J on a.id = J.honnan_id GROUP BY a.nev;

--Adott állomásról hány vonat indul
SELECT a.nev as allomas, COUNT(*) as darab FROM Allomasok a JOIN Menetrendek M on a.id = M.megallo_id GROUP BY a.nev;

--Adott állomásról hány utas indult
SELECT a.nev, COUNT(*) FROM Allomasok a JOIN Jegyek J on a.id = J.honnan_id GROUP BY J.honnan_id, a.nev;
