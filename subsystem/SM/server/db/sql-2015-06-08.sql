CREATE SCHEMA IF NOT EXISTS `db_zebra_sm` DEFAULT CHARACTER SET utf8 ;
use db_zebra_sm;

CREATE TABLE IF NOT EXISTS `db_zebra_sm`.`t_user` (
  `uid` INT  NOT NULL COMMENT '用户ID\n',
  `phone` INT NOT NULL COMMENT '用户手机号\n',
  `password` VARCHAR(50) NOT NULL COMMENT '密码\n',
  `create_time` TIMESTAMP NOT NULL DEFAULT NOW() COMMENT '帐户的创建时间 \n',
  PRIMARY KEY (`uid`),
  UNIQUE INDEX `phone_UNIQUE` (`phone` ASC))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COMMENT = '用户登录表';


CREATE TABLE IF NOT EXISTS `db_zebra_sm`.`t_user_info` (
  `uid` INT NOT NULL COMMENT '用户ID',
  `age` INT NULL COMMENT '年龄',
  `sex` INT NULL COMMENT '用户性别',
  `occupation` VARCHAR(50) NULL COMMENT '职业',
  `head` VARCHAR(50) NULL COMMENT '头像',
  `cert_id` VARCHAR(50) NULL COMMENT '身份证',
  `fraction` INT NOT NULL DEFAULT 0 COMMENT '用户积分',
  `level` INT NOT NULL DEFAULT 0 COMMENT '用户等级',
  PRIMARY KEY (`uid`),
  UNIQUE INDEX `cert_id_UNIQUE` (`cert_id` ASC))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


CREATE TABLE IF NOT EXISTS `db_zebra_sm`.`t_user_state` (
  `usr_id` INT NOT NULL,
  `online_state` INT NOT NULL DEFAULT 0 COMMENT '在线状态',
  `lng` DOUBLE UNSIGNED NOT NULL DEFAULT 999 COMMENT '经度',
  `lat` DOUBLE NOT NULL DEFAULT 999 COMMENT '纬度',
  `service_state` INT NOT NULL DEFAULT 0 COMMENT '服务状态',
  `is_debts` TINYINT(1) NOT NULL DEFAULT False COMMENT '是否欠费',
  PRIMARY KEY (`usr_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


CREATE TABLE IF NOT EXISTS `db_zebra_sm`.`t_service` (
  `sid` INT NOT NULL COMMENT '服务ID\n',
  `s_state` INT NOT NULL DEFAULT 0,
  `uid` INT NOT NULL,
  `did` INT NOT NULL,
  `mileage` INT NOT NULL DEFAULT 0,
  `start_time` TIMESTAMP NULL DEFAULT NOW(),
  `end_time` TIMESTAMP NULL,
  PRIMARY KEY (`sid`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8
COMMENT = '记录一次服务记录\n'





