


DROP TABLE IF EXISTS `Type`;
CREATE TABLE `Type`
(
	`id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	`title` VARCHAR(32) NOT NULL,
	`variable` VARCHAR(32) NOT NULL,
	`description` VARCHAR(256) NOT NULL
);

INSERT INTO `Type` (`title`, `variable`, `description`) VALUES
('Contributor', 'contributor', 'Programmer who adds to a project'),
('Administrator', 'administrator', 'Works at TPA'),
('Super', 'super', 'User with complete access');


DROP TABLE IF EXISTS `User`;
CREATE TABLE `User`
(
	`id` INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	`first_name` VARCHAR(32) NOT NULL,
	`last_name` VARCHAR(32) NOT NULL,
	`username` VARCHAR(32) NOT NULL,
	`email` VARCHAR(64) NOT NULL UNIQUE,
	`password` VARCHAR(32) NOT NULL,
	`picture` BLOB DEFAULT NULL,
	`website` VARCHAR(128) DEFAULT NULL,
	`location` VARCHAR(128) DEFAULT NULL,
	`info` TEXT DEFAULT NULL,
	`type_id` INT NOT NULL DEFAULT 1,
	FOREIGN KEY (`type_id`) REFERENCES `Type`(`id`)
);

INSERT INTO `User` (`first_name`, `last_name`, `username`, `email`, `password`, `website`, `location`, `info`, `type_id`) VALUES
('Mathew', 'Zinke', 'MPZinke', '', 'password', 'mathewzinke.com', 'Fort Worth, TX', 'I\'m awesome', 3);