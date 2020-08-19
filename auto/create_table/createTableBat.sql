
		DROP TABLE IF EXISTS `staff_info_mirror`;
		 CREATE TABLE `staff_info_mirror`  (
		 `staff_id` varchar(32) NOT NULL COMMENT '员工UUID:主键，按后端生成策略生成',
`id_card_num` varchar(50) NOT NULL COMMENT '身份证号码',
`is_assign` int(1) NULL DEFAULT NULL COMMENT '是否外派人员 0：否 1：是',
`assign_type` int(1) NULL DEFAULT NULL COMMENT '外派人员类型 0：外派财务负责人 1：外派产权代表',
`work_status` int(1) NULL DEFAULT NULL COMMENT '工作状态 0：在职 1：离职 2：退休',
`company_name` varchar(200) NULL DEFAULT NULL COMMENT '单位名称 (集团本部人员就填“集团本部”、集团中层干部中非集团本部的填其所在单位名称)',
`dept_name` varchar(100) NULL DEFAULT NULL COMMENT '部门',
`is_headquarters` int(1) NULL DEFAULT NULL COMMENT '是否集团本部人员 0：否 1：是',
`staff_name` varchar(50) NULL DEFAULT NULL COMMENT '姓名',
`gender` int(1) NULL DEFAULT NULL COMMENT '性别 0：女 1：男',
`nation` varchar(20) NULL DEFAULT NULL COMMENT '民族',
`native_place` varchar(20) NULL DEFAULT NULL COMMENT '籍贯',
`birthday` datetime NULL DEFAULT NULL COMMENT '出生年月',
`work_begin_date` datetime NULL DEFAULT NULL COMMENT '参加工作时间',
`join_date` datetime NULL DEFAULT NULL COMMENT '到集团本部时间',
`political_status` varchar(20) NULL DEFAULT NULL COMMENT '政治面貌',
`party_join_date` datetime NULL DEFAULT NULL COMMENT '入党时间',
`current_rank` varchar(50) NULL DEFAULT NULL COMMENT '现职级（退休人员的“原职务”也填到这里；离职人员的“职务”也填到这里。[新加字段，副处级])',
`current_rank_start_date` datetime NULL DEFAULT NULL COMMENT '任现职级时间（"中层干部表中的“任现职）',
`current_post` varchar(50) NULL DEFAULT NULL COMMENT '现岗位（这里只做记录)',
`assign_company` varchar(200) NULL DEFAULT NULL COMMENT '外派单位名称——{外派产权代表、外派财务负责人、非外派人员}',
`assign_job_title` varchar(50) NULL DEFAULT NULL COMMENT '外派职务——{对应外派表里的“单位”}',
`full_time_education` varchar(20) NULL DEFAULT NULL COMMENT '全日制最高学历',
`full_time_degree` varchar(20) NULL DEFAULT NULL COMMENT '全日制最高学位',
`full_time_graduated_school` varchar(300) NULL DEFAULT NULL COMMENT '全日制毕业院校',
`full_time_graduated_major` varchar(300) NULL DEFAULT NULL COMMENT '全日制毕业专业',
`professional_title_rank` int(1) NULL DEFAULT NULL COMMENT '职称级别 0:无 1:初级 2:中级 3:副高级 4:正高级',
`professional_title_name` varchar(50) NULL DEFAULT NULL COMMENT '职称/职业资格名称',
`telephone` varchar(50) NULL DEFAULT NULL COMMENT '电话号码',
`part_time_education` varchar(20) NULL DEFAULT NULL COMMENT '非全日制最高学历',
`part_time_degree` varchar(20) NULL DEFAULT NULL COMMENT '非全日制最高学位',
`part_time_graduated_school` varchar(300) NULL DEFAULT NULL COMMENT '全日制毕业院校',
`part_time_graduated_major` varchar(300) NULL DEFAULT NULL COMMENT '全日制毕业专业',
`top_education` varchar(50) NULL DEFAULT NULL COMMENT '最高学历',
`top_degree` varchar(50) NULL DEFAULT NULL COMMENT '最高学位',
`is_mid_level_cadres` int(1) NULL DEFAULT NULL COMMENT '是否集团中层干部 0：否 1：是（字段值设定长一点）'
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Compact;
SET FOREIGN_KEY_CHECKS = 1;
		DROP TABLE IF EXISTS `staff_cadres_mirror`;
		 CREATE TABLE `staff_cadres_mirror`  (
		 `staff_id` varchar(32) NOT NULL COMMENT '员工UUID:主键，按后端生成策略生成',
`id_card_num` varchar(50) NOT NULL COMMENT '身份证号码',
`work_status` int(1) NULL DEFAULT NULL COMMENT '工作状态 0：在职 1：离职 2：退休',
`company_name` varchar(200) NULL DEFAULT NULL COMMENT '单位名称 (集团本部人员就填“集团本部”、集团中层干部中非集团本部的填其所在单位名称)',
`dept_name` varchar(100) NULL DEFAULT NULL COMMENT '部门',
`is_headquarters` int(1) NULL DEFAULT NULL COMMENT '是否集团本部人员 0：否 1：是',
`staff_name` varchar(50) NULL DEFAULT NULL COMMENT '姓名',
`gender` int(1) NULL DEFAULT NULL COMMENT '性别 0：女 1：男',
`nation` varchar(20) NULL DEFAULT NULL COMMENT '民族',
`native_place` varchar(20) NULL DEFAULT NULL COMMENT '籍贯',
`birthday` datetime NULL DEFAULT NULL COMMENT '出生年月',
`work_begin_date` datetime NULL DEFAULT NULL COMMENT '参加工作时间',
`political_status` varchar(20) NULL DEFAULT NULL COMMENT '政治面貌',
`party_join_date` datetime NULL DEFAULT NULL COMMENT '入党时间',
`current_rank` varchar(50) NULL DEFAULT NULL COMMENT '现职级（退休人员的“原职务”也填到这里；离职人员的“职务”也填到这里。[新加字段，副处级])',
`current_rank_start_date` datetime NULL DEFAULT NULL COMMENT '任现职级时间（"中层干部表中的“任现职）',
`current_post` varchar(50) NULL DEFAULT NULL COMMENT '现岗位/现主要岗位（这里只做记录)',
`head_rank_start_date` datetime NULL DEFAULT NULL COMMENT '任正职级时间',
`deputy_rank_start_date` datetime NULL DEFAULT NULL COMMENT '任副职级时间',
`assign_company` varchar(200) NULL DEFAULT NULL COMMENT '外派单位名称——{外派产权代表、外派财务负责人、非外派人员}',
`assign_job_title` varchar(50) NULL DEFAULT NULL COMMENT '外派职务——{对应外派表里的“单位”}',
`full_time_education` varchar(20) NULL DEFAULT NULL COMMENT '全日制最高学历',
`full_time_degree` varchar(20) NULL DEFAULT NULL COMMENT '全日制最高学位',
`full_time_graduated_school` varchar(300) NULL DEFAULT NULL COMMENT '全日制毕业院校',
`full_time_graduated_major` varchar(300) NULL DEFAULT NULL COMMENT '全日制毕业专业',
`professional_title_rank` int(1) NULL DEFAULT NULL COMMENT '职称级别 0:无 1:初级 2:中级 3:副高级 4:正高级',
`professional_title_name` varchar(50) NULL DEFAULT NULL COMMENT '职称/职业资格名称',
`telephone` varchar(50) NULL DEFAULT NULL COMMENT '电话号码',
`part_time_education` varchar(20) NULL DEFAULT NULL COMMENT '非全日制最高学历',
`part_time_degree` varchar(20) NULL DEFAULT NULL COMMENT '非全日制最高学位',
`part_time_graduated_school` varchar(300) NULL DEFAULT NULL COMMENT '全日制毕业院校',
`part_time_graduated_major` varchar(300) NULL DEFAULT NULL COMMENT '全日制毕业专业',
`top_education` varchar(50) NULL DEFAULT NULL COMMENT '最高学历',
`top_degree` varchar(50) NULL DEFAULT NULL COMMENT '最高学位',
`is_mid_level_cadres` int(1) NULL DEFAULT NULL COMMENT '是否集团中层干部 0：否 1：是（字段值设定长一点）',
`is_reserved_rank` int(1) NULL DEFAULT NULL COMMENT '是否保留职级 0：否 1：是（字段值设定长一点）',
`is_preferential` int(1) NULL DEFAULT NULL COMMENT '是否享受待遇 0：否 1：是（字段值设定长一点）',
`identity_attribute` int(1) NULL DEFAULT NULL COMMENT '身份属性 0: 干部 1：成员企业高管 2：成员企业高官正职 3：成员企业高管副职',
`adjust_date` datetime NULL DEFAULT NULL COMMENT '变动时间',
`adjust_type` int(1) NULL DEFAULT NULL COMMENT '变动类型 0: 辞职 1：免职 2：降职',
`retired_date` datetime NULL DEFAULT NULL COMMENT '退休时间',
`death_date` datetime NULL DEFAULT NULL COMMENT '去世时间',
`alive` int(1) NULL DEFAULT NULL COMMENT '是否在世人员 0：否 1：是'
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Compact;
SET FOREIGN_KEY_CHECKS = 1;
		DROP TABLE IF EXISTS `department`;
		 CREATE TABLE `department`  (
		 `id` varchar(32) NOT NULL COMMENT '部门UUID:主键，按后端生成策略生成',
`department_name` varchar(200) NULL DEFAULT NULL COMMENT '部门名称',
`department_number` varchar(32) NULL DEFAULT NULL COMMENT '部门编号',
`company_number` varchar(32) NULL DEFAULT NULL COMMENT '公司编号',
`department_staff_size` int(2) NOT NULL COMMENT '部门编制个数',
`data_status` int(1) NULL DEFAULT NULL COMMENT '数据状态 0：不可用 1：可用'
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Compact;
SET FOREIGN_KEY_CHECKS = 1;
		DROP TABLE IF EXISTS `company_senior_executives`;
		 CREATE TABLE `company_senior_executives`  (
		 `id` varchar(32) NOT NULL COMMENT 'UUID:主键，按后端生成策略生成',
`company_name` varchar(200) NULL DEFAULT NULL COMMENT '单位名称',
`relate_leader` varchar(200) NULL DEFAULT NULL COMMENT '分工联系的集团领导',
`legal_representative` varchar(200) NULL DEFAULT NULL COMMENT '法定代表人',
`chairman` varchar(200) NULL DEFAULT NULL COMMENT '董事长',
`deputy_chairman` varchar(200) NULL DEFAULT NULL COMMENT '副董事长',
`director` varchar(200) NULL DEFAULT NULL COMMENT '董事',
`independent_director` varchar(200) NULL DEFAULT NULL COMMENT '独立董事',
`chairman_supervisor` varchar(200) NULL DEFAULT NULL COMMENT '监事会主席',
`supervisor` varchar(200) NULL DEFAULT NULL COMMENT '监事',
`general_manager` varchar(200) NULL DEFAULT NULL COMMENT '总经理',
`deputy_manager` varchar(200) NULL DEFAULT NULL COMMENT '副总经理',
`party_committee_secretary` varchar(200) NULL DEFAULT NULL COMMENT '党委书记',
`party_general_branch_secretary` varchar(200) NULL DEFAULT NULL COMMENT '党总支书记',
`party_branch_secretary` varchar(200) NULL DEFAULT NULL COMMENT '党支部书记',
`deputy_secretary_party_committee` varchar(200) NULL DEFAULT NULL COMMENT '专职或主持工作党委副书记',
`commission_discipline_inspection` varchar(200) NULL DEFAULT NULL COMMENT '纪委书记',
`description` varchar(200) NULL DEFAULT NULL COMMENT '说明'
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Compact;
SET FOREIGN_KEY_CHECKS = 1;
		DROP TABLE IF EXISTS `staff_concurrent_post`;
		 CREATE TABLE `staff_concurrent_post`  (
		 `id` varchar(32) NOT NULL COMMENT 'UUID:主键，按后端生成策略生成',
`staff_name` varchar(50) NULL DEFAULT NULL COMMENT '姓名',
`company_name` varchar(200) NULL DEFAULT NULL COMMENT '单位名称',
`current_post` varchar(50) NULL DEFAULT NULL COMMENT '现岗位/现主要岗位（这里只做记录)',
`begin_date` datetime NULL DEFAULT NULL COMMENT '开始时间',
`end_date` datetime NULL DEFAULT NULL COMMENT '结束时间',
`currently` int(1) NULL DEFAULT NULL COMMENT '是否现任 0：否 1：是'
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Compact;
SET FOREIGN_KEY_CHECKS = 1;
		DROP TABLE IF EXISTS `post`;
		 CREATE TABLE `post`  (
		 `id` varchar(32) NOT NULL COMMENT '岗位UUID:主键，按后端生成策略生成',
`post_name` varchar(200) NULL DEFAULT NULL COMMENT '岗位名称',
`post_number` varchar(32) NULL DEFAULT NULL COMMENT '岗位编号',
`department_number` varchar(32) NULL DEFAULT NULL COMMENT '部门编号',
`post_staff_size` int(2) NOT NULL COMMENT '岗位编制个数',
`data_status` int(1) NULL DEFAULT NULL COMMENT '数据状态 0：不可用 1：可用'
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Compact;
SET FOREIGN_KEY_CHECKS = 1;
		DROP TABLE IF EXISTS `company`;
		 CREATE TABLE `company`  (
		 `id` varchar(32) NOT NULL COMMENT '公司UUID:主键，按后端生成策略生成',
`company_name` varchar(200) NULL DEFAULT NULL COMMENT '公司名称',
`company_number` varchar(32) NULL DEFAULT NULL COMMENT '公司编号',
`parent_company_number` varchar(32) NULL DEFAULT NULL COMMENT '父公司编号',
`data_status` int(1) NULL DEFAULT NULL COMMENT '数据状态 0：不可用 1：可用'
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Compact;
SET FOREIGN_KEY_CHECKS = 1;