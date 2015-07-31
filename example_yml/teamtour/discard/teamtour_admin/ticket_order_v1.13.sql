use `ticket_order`;
INSERT INTO `config` (`config_key`, `config_value`)
VALUES ('sms_warning_money', '');
INSERT INTO `config` (`config_key`, `config_value`)
VALUES ('sms_warning_send_email', '');
INSERT INTO `config` (`config_key`, `config_value`)
VALUES ('sms_warning_send', '0');
/*fix orders中的产品类型*/
UPDATE orders SET kind = 3 WHERE (length(ticket_infos)-length(replace(ticket_infos,'base_id','')))>7;

/*购物车添加旅客信息字段*/
ALTER TABLE `cart` ADD `visitors` text COLLATE utf8_unicode_ci COMMENT '旅客信息（json二维数组，姓名，手机，身份证）';

/*订单表添加*/
ALTER TABLE `orders` ADD `need_idcard` tinyint(1) unsigned NOT NULL DEFAULT '0' COMMENT '是否旅客身份证必填，1是，0否' AFTER `message_open`;
