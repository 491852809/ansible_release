/* 4:09:11 PM 192.168.1.14 */ ALTER TABLE `users` ADD `login_duration` INT(11)  NULL  DEFAULT '3600'  COMMENT '登录超时';
CREATE TABLE `supply_user_login_duration` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `login_duration` int(11) DEFAULT '3600' COMMENT '登录超时',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
