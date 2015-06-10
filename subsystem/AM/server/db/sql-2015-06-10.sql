/*
Navicat MySQL Data Transfer

Source Server         : 10.111.32.95
Source Server Version : 50541
Source Host           : 10.111.32.95:3306
Source Database       : db_zebra_am

Target Server Type    : MYSQL
Target Server Version : 50541
File Encoding         : 65001

Date: 2015-06-10 16:12:15
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `t_account`
-- ----------------------------
DROP TABLE IF EXISTS `t_account`;
CREATE TABLE `t_account` (
  `accid` int(11) NOT NULL AUTO_INCREMENT,
  `remain` double NOT NULL DEFAULT '0',
  `create_time` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00' ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`accid`)
) ENGINE=InnoDB AUTO_INCREMENT=100000001  DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of t_account
-- ----------------------------
