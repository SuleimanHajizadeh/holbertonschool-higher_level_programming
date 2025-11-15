-- 100-move_to_utf8.sql
-- hbtn_0c_0 bazası, first_table cədvəli və name sütunu UTF8-ə çevrilir

-- Database charset və collate dəyişir
ALTER DATABASE hbtn_0c_0 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci;

-- Table charset və collate dəyişir
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Field name charset və collate dəyişir (əgər table convert etməsə belə)
ALTER TABLE first_table MODIFY name VARCHAR(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
