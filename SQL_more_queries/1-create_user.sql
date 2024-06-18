-- Script that creates a user in MYSQL server.
-- Step 1: Check if the user already exists
-- We're using the `mysql` database to check the `user` table.
SELECT IF(COUNT(*) = 0, 'User does not exist', 'User exists') INTO @user_exists
FROM mysql.user
WHERE user = 'user_0d_1' AND host = '%';

-- Step 2: Create the user if they do not exist
-- Only create the user if @user_exists is 'User does not exist'
SET @create_user = IF(@user_exists = 'User does not exist',
                      'CREATE USER \'user_0d_1\'@\'%\' IDENTIFIED BY \'user_0d_1_pwd\';',
                      'SELECT "User already exists, skipping creation";');

PREPARE stmt FROM @create_user;
EXECUTE stmt;
DEALLOCATE PREPARE stmt;

-- Step 3: Grant all privileges to the user
-- This is safe to run whether the user was just created or already existed
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'%' WITH GRANT OPTION;

-- Step 4: Apply the changes
FLUSH PRIVILEGES;
