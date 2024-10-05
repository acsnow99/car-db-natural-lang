-- Table for Car
CREATE TABLE Car (
    VIN CHAR(17) PRIMARY KEY,  -- Vehicle Identification Number as the primary key
    cityCode CHAR(6),          -- Foreign key linking to the City table
    licensePlate CHAR(7)       -- License plate number
);

-- Table for City
CREATE TABLE City (
    cityCode CHAR(6) PRIMARY KEY -- City code as the primary key
);

-- Table for Landmark
CREATE TABLE Landmark (
    landmarkId INTEGER PRIMARY KEY AUTOINCREMENT,
    cityCode CHAR(6),            -- Foreign key linking to the City table
    location VARCHAR(25),        -- Name of the landmark location
    FOREIGN KEY (cityCode) REFERENCES City(cityCode) -- Ensure referential integrity
);

-- Table for Rider
CREATE TABLE Rider (
    userId INTEGER PRIMARY KEY AUTOINCREMENT -- Unique user ID, auto-incremented
);

-- Updated Table for Ride Record with Foreign Keys to Landmark
CREATE TABLE RideRecord (
    rideId INTEGER PRIMARY KEY AUTOINCREMENT, -- Unique ride ID, auto-incremented
    pickupLandmarkId INTEGER,         
    dropLandmarkId INTEGER,                 -- Name of the drop-off landmark location
    userId INTEGER,                           -- Foreign key referencing Rider
    VIN CHAR(17),                             -- Foreign key referencing Car
    FOREIGN KEY (userId) REFERENCES Rider(userId), -- Link to Rider table
    FOREIGN KEY (VIN) REFERENCES Car(VIN),        -- Link to Car table
    FOREIGN KEY (pickupLandmarkId) 
        REFERENCES Landmark(landmarkId),  -- Link pickup to Landmark table
    FOREIGN KEY (dropLandmarkId) 
        REFERENCES Landmark(landmarkId)   -- Link drop-off to Landmark table
);




-- Insert statements for the City table
INSERT INTO City (cityCode) VALUES
('NYC'),
('LAX'),
('CHI'),
('HOU'),
('PHX'),
('DAL'),
('ATL'),
('MIA'),
('SEA'),
('BOS');

-- Insert statements for the Landmark table
INSERT INTO Landmark (cityCode, location) VALUES
('NYC', 'Statue of Liberty'),
('NYC', 'Central Park'),
('LAX', 'Hollywood Sign'),
('CHI', 'Millennium Park'),
('HOU', 'Space Center Houston'),
('PHX', 'Desert Botanical Garden'),
('DAL', 'Dealey Plaza'),
('ATL', 'Georgia Aquarium'),
('MIA', 'South Beach'),
('SEA', 'Pike Place Market');

-- Insert statements for the Car table
INSERT INTO Car (VIN, cityCode, licensePlate) VALUES
('1HGCM82633A123456', 'NYC', 'NY1234'),
('1HGCM82633A123457', 'LAX', 'LA1234'),
('1HGCM82633A123458', 'CHI', 'CH1234'),
('1HGCM82633A123459', 'HOU', 'HO1234'),
('1HGCM82633A123450', 'PHX', 'PH1234'),
('1HGCM82633A123451', 'DAL', 'DA1234'),
('1HGCM82633A123452', 'ATL', 'AT1234'),
('1HGCM82633A123453', 'MIA', 'MI1234'),
('1HGCM82633A123454', 'SEA', 'SE1234'),
('1HGCM82633A123455', 'BOS', 'BO1234');

-- Insert statements for the Rider table
INSERT INTO Rider (userId) VALUES
(1),
(2),
(3),
(4),
(5),
(6),
(7),
(8),
(9),
(10);

-- Insert statements for the RideRecord table
INSERT INTO RideRecord (pickupLandmarkId, dropLandmarkId, userId, VIN) VALUES
(1, 2, 1, '1HGCM82633A123456'),  -- Statue of Liberty to Central Park
(3, 4, 2, '1HGCM82633A123457'),  -- Hollywood Sign to Millennium Park
(5, 6, 3, '1HGCM82633A123458'),  -- Space Center Houston to Desert Botanical Garden
(7, 8, 4, '1HGCM82633A123459'),  -- Dealey Plaza to Georgia Aquarium
(9, 10, 5, '1HGCM82633A123450'),  -- South Beach to Pike Place Market
(1, 3, 6, '1HGCM82633A123451'),   -- Statue of Liberty to Hollywood Sign
(4, 5, 7, '1HGCM82633A123452'),   -- Millennium Park to Space Center Houston
(6, 7, 8, '1HGCM82633A123453'),   -- Desert Botanical Garden to Dealey Plaza
(8, 9, 9, '1HGCM82633A123454'),   -- Georgia Aquarium to South Beach
(10, 1, 10, '1HGCM82633A123455');  -- Pike Place Market to Statue of Liberty

