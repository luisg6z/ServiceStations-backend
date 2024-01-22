CREATE DOMAIN email_domain AS
    VARCHAR(255)
    CHECK(VALUE ~* '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}$');

CREATE DOMAIN phone_domain AS
    VARCHAR(10)
    CHECK(VALUE ~ '^[0-9]{10}$');


CREATE TABLE Drivers(                            ----1Conductor----
    driver_id VARCHAR(10) NOT NULL,
    driver_name VARCHAR(30) NOT NULL,
    PRIMARY KEY(driver_id)
);

CREATE TABLE TankerTrucks(                      ----2Camiones Cisterna----
    plateTT VARCHAR(8) NOT NULL,
    capacity_lit INT NOT NULL,
    PRIMARY KEY(plateTT),
    CONSTRAINT const_capacity_lit CHECK(capacity_lit > 0)
);

CREATE TABLE Modalities(                        ----3Modalidades---
    modality_id SERIAL, --ojito aca
    descrpt VARCHAR(20) NOT NULL,
    PRIMARY KEY(modality_id)
);

CREATE TABLE States(                             ---4Estado----
    state_id SERIAL,
    state_name VARCHAR(20) NOT NULL,
    PRIMARY KEY(state_id),
    CONSTRAINT const_state_name UNIQUE(state_name)
);

CREATE TABLE Cities(                              ---5Ciudades---
    city_id SERIAL,
    city_name VARCHAR(20) NOT NULL,
    state_id INT NOT NULL,
    modality_id INT NOT NULL,
    PRIMARY KEY(city_id),
    FOREIGN KEY(state_id) REFERENCES States(state_id)
        ON DELETE RESTRICT,
    FOREIGN KEY(modality_id) REFERENCES Modalities(modality_id)
);

CREATE TABLE Employees(                             ---6 Empleados---
    emp_id VARCHAR(10) NOT NULL,
    first_name VARCHAR(20) NOT NULL,
    last_name VARCHAR(20) NOT NULL,
    adress VARCHAR(100) NOT NULL,
    email email_domain NOT NULL,
    PRIMARY KEY(emp_id)
);

CREATE TABLE ServiceStations(                       ---7Estacion de Servicio---
    station_rif VARCHAR(11) NOT NULL,
    adress VARCHAR(100) NOT NULL,
    amount_of_fuel INT NOT NULL,
    payment_type CHAR NOT NULL,
    station_name VARCHAR(50) NOT NULL,
    city_id INT NOT NULL,
    manager_id VARCHAR(10) NOT NULL,
    manager_start_date DATE NOT NULL,
    PRIMARY KEY(station_rif),
    FOREIGN KEY(city_id) REFERENCES Cities(city_id)
        ON DELETE RESTRICT,
    FOREIGN KEY(manager_id) REFERENCES Employees(emp_id)
        ON DELETE RESTRICT,
    CONSTRAINT const_payment_station CHECK(payment_type = 'D' OR payment_type = 'S')
);

CREATE TABLE Owners(                                ---8 Propietarios---
    owner_id VARCHAR(10) NOT NULL,
    email email_domain NOT NULL,
    owner_name VARCHAR(50) NOT NULL,
    PRIMARY KEY(owner_id)
);

CREATE TABLE Vehicles(                              ---10Vehiculos---
    plate VARCHAR(8) NOT NULL,
    model VARCHAR(15) NOT NULL,
    capacity INT NOT NULL,
    year_release INT NOT NULL,
    serial_bodywork VARCHAR(30) NOT NULL,
    serial_chassis VARCHAR(30) NOT NULL,
    owner_id VARCHAR(10) NOT NULL,
    PRIMARY KEY(plate),
    FOREIGN KEY(owner_id) REFERENCES Owners(owner_id)
        ON DELETE RESTRICT,
    FOREIGN KEY(model) REFERENCES Models(model_name)
        ON DELETE RESTRICT,
    CONSTRAINT const_serial_bodywork UNIQUE(serial_bodywork),
    CONSTRAINT const_serial_chassis UNIQUE(serial_chassis),
    CONSTRAINT const_capacity CHECK( capacity > 0),
    CONSTRAINT const_year_release CHECK (year_release <= 2024)
);

CREATE TABLE Payments(                             ---13Pagos---
    payment_id SERIAL,
    payment_date DATE NOT NULL,
    amount REAL NOT NULL,
    payment_type CHAR NOT NULL,
    card_number VARCHAR(24),
    bank VARCHAR(30), 
    currency CHAR NOT NULL,
    station_rif VARCHAR(11) NOT NULL,
    plate VARCHAR(8) NOT NULL,
    PRIMARY KEY(payment_id),
    FOREIGN KEY(payment_date) REFERENCES Rates(rate_date)
        ON DELETE RESTRICT,
    FOREIGN KEY(station_rif, plate, payment_date) REFERENCES Dispatched(station_rif, plate, dispatch_date)
        ON DELETE RESTRICT,
    CONSTRAINT const_payment_type CHECK(payment_type = 'E' OR payment_type = 'T'),
    CONSTRAINT const_currency CHECK(currency = 'B' OR currency = 'D'),
    CONSTRAINT const_card_number CHECK(card_number ~ '^[0-9]{16}$'),
    CONSTRAINT const_amount CHECK(amount > 0)
);

CREATE TABLE Rates(                         ---11 Tasa---
    rate_date DATE NOT NULL,
    rates_value REAL NOT NULL,
    PRIMARY KEY (rate_date),
    CONSTRAINT const_rate_value CHECK(rates_value > 0)
);

CREATE TABLE Dispatched(                   ---12Se envia--- 
    station_rif VARCHAR(11) NOT NULL,
    plate VARCHAR(8) NOT NULL,
    dispatch_date DATE NOT NULL,
    liters REAL NOT NULL,
    Bs REAL,
    PRIMARY KEY (station_rif, plate, dispatch_date),
    FOREIGN KEY (station_rif) REFERENCES ServiceStations (station_rif)
        ON DELETE RESTRICT,
    FOREIGN KEY (plate) REFERENCES  Vehicles(plate)
        ON DELETE RESTRICT,
    CONSTRAINT const_bs CHECK(bs > 0)
);

CREATE TABLE WorksIn (                      ---14Trabaja en----
    station_rif VARCHAR (11) NOT NULL,
    emp_id VARCHAR(10) NOT NULL,
    PRIMARY KEY (station_rif , emp_id),
    FOREIGN KEY (station_rif) REFERENCES ServiceStations (station_rif)
        ON DELETE CASCADE,
    FOREIGN KEY (emp_id) REFERENCES Employees(emp_id)
        ON DELETE CASCADE
);

CREATE TABLE Supplies (                     ----16Surte----
    station_rif VARCHAR(11) NOT NULL,
    Supplies_date DATE NOT NULL,
    liters REAL NOT NULL,
    driver_id VARCHAR(10),
    plateTT VARCHAR(8) NOT NULL,
    PRIMARY KEY (station_rif, plateTT, Supplies_date, driver_id),
    FOREIGN KEY (station_rif) REFERENCES ServiceStations (station_rif)
        ON DELETE RESTRICT,
    FOREIGN KEY (plateTT) REFERENCES TankerTrucks(plateTT)
        ON DELETE RESTRICT,
    FOREIGN KEY (driver_id) REFERENCES Drivers(driver_id)
        ON DELETE RESTRICT,
    CONSTRAINT const_liters CHECK(liters > 0)
);


CREATE TABLE Applies(                       ---17Aplica---
    modality_id INT NOT NULL,
    city_id INT NOT NULL,
    aplies_start_date DATE NOT NULL,
    aplies_End_date DATE,
    PRIMARY KEY (modality_id,city_id,aplies_start_date),
    FOREIGN KEY (modality_id) REFERENCES Modalities(modality_id)
        ON DELETE CASCADE,
    FOREIGN KEY (city_id) REFERENCES Cities (city_id)
        ON DELETE CASCADE
);

CREATE TABLE Drives(                                           ---15Conduce----
    driver_id VARCHAR(10) NOT NULL,
    plateTT VARCHAR(8) NOT NULL,
    PRIMARY KEY (driver_id, plateTT),
    FOREIGN KEY (driver_id) REFERENCES Drivers(driver_id)
        ON DELETE CASCADE,
    FOREIGN KEY (plateTT) REFERENCES TankerTrucks (plateTT)
        ON DELETE CASCADE
);

CREATE TABLE EmployeesPhones(                             ---18 Telefonos de empleados----
    emp_id VARCHAR(10) NOT NULL,
    phone_number_emp phone_domain NOT NULL,
    PRIMARY KEY (emp_id, phone_number_emp),
    FOREIGN KEY (emp_id) REFERENCES Employees (emp_id)
        ON DELETE CASCADE
);

CREATE TABLE OwnersPhones (                                 ---19Telefonos de propietario----
    owner_id VARCHAR(10) NOT NULL,
    phone_number_own phone_domain NOT NULL,
    PRIMARY KEY (owner_id, phone_number_own),
    FOREIGN KEY (owner_id) REFERENCES Owners (owner_id)
        ON DELETE CASCADE
);
CREATE TABLE Models (                                       ---9Modelos---- 
    model_name VARCHAR(30) NOT Null,
    brand VARCHAR(30) NOT NULL,
    type_vehicle CHAR NOT NULL,
	PRIMARY KEY (model_name),
    CONSTRAINT const_type_vehicle CHECK(type_vehicle = 'C' OR type_vehicle = 'M')
);

                                                            ---Historico Suministros---

CREATE TABLE Historic_supplies(
    station_rif VARCHAR(11) NOT NULL,
    supplies_date DATE NOT NULL,
    liters REAL NOT NULL,
    driver_id VARCHAR(10),
    plateTT VARCHAR(8) NOT NULL,
    PRIMARY KEY (station_rif, plateTT, Supplies_date, driver_id)
);

                                                            ---Historico Despachos ---

CREATE TABLE Historic_dispatched(
    station_rif VARCHAR(11) NOT NULL,
    plate VARCHAR(8) NOT NULL,
    dispatch_date DATE NOT NULL,
    liters REAL NOT NULL,
    Bs REAL,
    PRIMARY KEY (station_rif, plate, dispatch_date)
);

--Trigger cuando ocurre un despacho


CREATE OR REPLACE FUNCTION decrement_fuel()
RETURNS TRIGGER AS $$
BEGIN
  UPDATE ServiceStations SET amount_of_fuel = amount_of_fuel - CAST(NEW.liters AS INTEGER)
  WHERE station_rif = NEW.station_rif;
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER decrement_trigger
AFTER INSERT ON Dispatched
FOR EACH ROW
EXECUTE FUNCTION decrement_fuel();

--trigger para el aumento cuando ocurre un suministro

CREATE OR REPLACE FUNCTION raise_fuel()
RETURNS TRIGGER AS $$
BEGIN
  UPDATE ServiceStations SET amount_of_fuel = amount_of_fuel + CAST(NEW.liters AS INTEGER)
  WHERE station_rif = NEW.station_rif;
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER raise_trigger
AFTER INSERT ON Supplies
FOR EACH ROW
EXECUTE FUNCTION raise_fuel();

--TRIGGER PARA INSERTAR EN HISTORICOS DE SUMINISTROS

CREATE OR REPLACE FUNCTION insert_historic_supplies() RETURNS TRIGGER AS $$
BEGIN
    INSERT INTO historic_supplies (station_rif, supplies_date, liters, driver_id, plateTT)
    VALUES (OLD.station_rif, OLD.supplies_date, OLD.liters, OLD.driver_id, OLD.plateTT);
    RETURN OLD;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_name
AFTER DELETE OR UPDATE ON supplies
FOR EACH ROW
EXECUTE FUNCTION insert_historic_supplies();

--TRIGGER PARA INSERTAR EN HISTORICOS DE SUMINISTROS

CREATE OR REPLACE FUNCTION insert_historic_dispatched() RETURNS TRIGGER AS $$
BEGIN
    INSERT INTO historic_dispatched (station_rif, plate, dispatch_date, liters, bs)
    VALUES (OLD.station_rif, OLD.plate, OLD.dispatch_date, OLD.liters, OLD.bs);
    RETURN OLD;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_name
AFTER DELETE OR UPDATE ON dispatched
FOR EACH ROW
EXECUTE FUNCTION insert_historic_dispatched();