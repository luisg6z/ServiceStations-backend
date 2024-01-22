alter table supplies drop constraint supplies_driver_id_fkey;

ALTER TABLE payments DROP CONSTRAINT payments_station_rif_fkey;
ALTER TABLE payments DROP CONSTRAINT payments_plate_fkey;
ALTER TABLE supplies ADD CONSTRAINT supplies_plate_fkey FOREIGN KEY(plateTT) REFERENCES TankerTrucks(plateTT);