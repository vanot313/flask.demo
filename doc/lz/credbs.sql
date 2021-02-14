/*==============================================================*/
/* DBMS name:      MySQL 5.0                                    */
/* Created on:     2021/2/13 23:37:23                           */
/*==============================================================*/


drop table if exists t_expert_apply;

drop table if exists t_log;

drop table if exists t_login_log;

drop table if exists t_menu;

drop table if exists t_role;

drop table if exists t_role_menu;

drop table if exists t_user;

drop table if exists t_user_role;

/*==============================================================*/
/* Table: t_expert_apply                                        */
/*==============================================================*/
create table t_expert_apply
(
   APPLY_ID             bigint(20)
);

/*==============================================================*/
/* Table: t_log                                                 */
/*==============================================================*/
create table t_log
(
   ID                   bigint(20) not null auto_increment comment '日志ID',
   USERNAME             varchar(50) character set utf8,
   OPERATION            text character set utf8,
   TIME                 decimal(11, 0) default NULL comment '耗时',
   METHOD               text character set utf8,
   PARAMS               text character set utf8,
   IP                   varchar(64) character set utf8,
   CREATE_TIME          datetime,
   location             varchar(50) character set utf8,
   primary key (ID),
   key t_log_create_time (CREATE_TIME)
)
ENGINE = MyISAM AUTO_INCREMENT = 1011 CHARACTER SET = utf8 COLLATE = utf8_general_ci COMMENT = '操作日志表' ROW_FORMAT = Dynamic;

/*==============================================================*/
/* Table: t_login_log                                           */
/*==============================================================*/
create table t_login_log
(
   ID                   bigint(11) not null auto_increment comment 'id',
   USERNAME             varchar(50) character set utf8,
   LOGIN_TIME           datetime,
   LOCATION             varchar(50) character set utf8,
   IP                   varchar(50) character set utf8,
   SYSTEM               varchar(50) character set utf8,
   BROWSER              varchar(50) character set utf8,
   primary key (ID),
   key t_login_log_login_time (LOGIN_TIME)
)
ENGINE = MyISAM AUTO_INCREMENT = 70 CHARACTER SET = utf8 COLLATE = utf8_general_ci COMMENT = '登录日志表' ROW_FORMAT = Dynamic;

/*==============================================================*/
/* Table: t_menu                                                */
/*==============================================================*/
create table t_menu
(
   MENU_ID              bigint(20) not null auto_increment comment '菜单/按钮ID',
   PARENT_ID            bigint(20) not null comment '上级菜单ID',
   MENU_NAME            varchar(50) not null comment '菜单/按钮名称',
   URL                  varchar(50) default NULL comment '菜单URL',
   PERMS                text comment '权限标识',
   ICON                 varchar(50) default NULL comment '图标',
   TYPE                 char(2) not null comment '类型 0菜单 1按钮',
   ORDER_NUM            bigint(20) default NULL comment '排序',
   CREATE_TIME          datetime not null comment '创建时间',
   MODIFY_TIME          datetime default NULL comment '修改时间',
   primary key (MENU_ID),
   key t_menu_parent_id (PARENT_ID),
   key t_menu_menu_id (MENU_ID)
)
ENGINE=InnoDB AUTO_INCREMENT=179 DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC COMMENT='菜单表';

/*==============================================================*/
/* Table: t_role                                                */
/*==============================================================*/
create table t_role
(
   ROLE_ID              bigint(20) not null auto_increment comment '角色ID',
   ROLE_NAME            varchar(100) character set utf8,
   REMARK               varchar(100) character set utf8,
   CREATE_TIME          datetime,
   MODIFY_TIME          datetime,
   primary key (ROLE_ID)
)
ENGINE = InnoDB AUTO_INCREMENT = 81 CHARACTER SET = utf8 COLLATE = utf8_general_ci COMMENT = '角色表' ROW_FORMAT = Dynamic;

/*==============================================================*/
/* Table: t_role_menu                                           */
/*==============================================================*/
create table t_role_menu
(
   ROLE_ID              bigint(20) not null comment '角色ID',
   MENU_ID              bigint(20) not null comment '菜单/按钮ID',
   key t_role_menu_menu_id (MENU_ID),
   key t_role_menu_role_id (ROLE_ID)
)
ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC COMMENT='角色菜单关联表';

/*==============================================================*/
/* Table: t_user                                                */
/*==============================================================*/
create table t_user
(
   USER_ID              bigint(20) not null auto_increment comment '用户ID',
   USERNAME             varchar(50) character set utf8,
   PASSWORD             varchar(128) character set utf8,
   EMAIL                varchar(128) character set utf8,
   MOBILE               varchar(20) character set utf8,
   STATUS               char(1) character set utf8,
   CREATE_TIME          datetime,
   MODIFY_TIME          datetime,
   LAST_LOGIN_TIME      datetime,
   SSEX                 char(1) character set utf8,
   IS_TAB               char(1) character set utf8,
   THEME                varchar(10) character set utf8,
   AVATAR               varchar(100) character set utf8,
   DESCRIPTION          varchar(100) character set utf8,
   primary key (USER_ID),
   key t_user_username (USERNAME),
   key t_user_mobile (MOBILE)
)
ENGINE = InnoDB AUTO_INCREMENT = 8 CHARACTER SET = utf8 COLLATE = utf8_general_ci COMMENT = '用户表' ROW_FORMAT = Dynamic;

/*==============================================================*/
/* Table: t_user_role                                           */
/*==============================================================*/
create table t_user_role
(
   USER_ID              bigint(20) not null comment '用户ID',
   ROLE_ID              bigint(20) not null comment '角色ID',
   key t_user_role_user_id (USER_ID),
   key t_user_role_role_id (ROLE_ID)
)
ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci COMMENT = '用户角色关联表' ROW_FORMAT = Dynamic;

