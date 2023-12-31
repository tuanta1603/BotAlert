-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Máy chủ: 127.0.0.1
-- Thời gian đã tạo: Th12 31, 2023 lúc 04:39 PM
-- Phiên bản máy phục vụ: 10.4.32-MariaDB
-- Phiên bản PHP: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Cơ sở dữ liệu: `trading_api`
--

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `bot_alert`
--

CREATE TABLE `bot_alert` (
  `id` int(11) NOT NULL,
  `syminfo` varchar(255) DEFAULT NULL,
  `prefix` varchar(255) DEFAULT NULL,
  `ticker` varchar(255) DEFAULT NULL,
  `basecurrency` varchar(255) DEFAULT NULL,
  `currency` varchar(255) DEFAULT NULL,
  `timeframe` varchar(255) DEFAULT NULL,
  `side` varchar(255) DEFAULT NULL,
  `position` varchar(255) DEFAULT NULL,
  `Action` varchar(255) DEFAULT NULL,
  `prices_pos` varchar(255) DEFAULT NULL,
  `prices_tp` varchar(255) DEFAULT NULL,
  `precent_tp` varchar(255) DEFAULT NULL,
  `pos_leverage` varchar(255) DEFAULT NULL,
  `pos_currency` varchar(255) DEFAULT NULL,
  `pos_quantity` varchar(255) DEFAULT NULL,
  `CurrencyManual` varchar(255) DEFAULT NULL,
  `QuantityManual` varchar(255) DEFAULT NULL,
  `codename` varchar(255) DEFAULT NULL,
  `type` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `bot_alert`
--

INSERT INTO `bot_alert` (`id`, `syminfo`, `prefix`, `ticker`, `basecurrency`, `currency`, `timeframe`, `side`, `position`, `Action`, `prices_pos`, `prices_tp`, `precent_tp`, `pos_leverage`, `pos_currency`, `pos_quantity`, `CurrencyManual`, `QuantityManual`, `codename`, `type`) VALUES
(1, 'aaaaa', 'dddd', 'dddd', 'ddddd', 'aaaaaa', 'ffffff', 'gggggggg', 'sssssss', 'sssssssssssss', 'eeeeeeeeeeeee', 'rrrrrrrrrrrrrrrrrrrrr', 'rrrrrrrrrrrrrr', 'rrrrrrrrrrrrr', 'rrrrrrrrrrr', 'eeeeeeeeeeeeeeeeeeee', 'eeeeeeeeeeeeeeee', 'eeeeeeeeeeee', 'eeeeeeeeeeeeeee', 'wwwwwwwwwwwwwwwwwwwwwwww'),
(5, 'string', 'string', 'string', 'string', 'string', 'string', 'string', 'string', 'string', 'string', 'string', 'string', 'string', 'string', 'string', 'string', 'string', 'string', 'string'),
(6, '1111', 'string', 'string', 'string', 'string', 'string', 'string', 'string', 'string', 'string', 'string', 'string', 'string', 'string', 'string', 'string', 'string', 'string', 'string'),
(7, 'string', 'string', 'string', 'string', 'string', 'string', 'string', 'string', 'string', 'string', 'string', 'string', 'string', 'string', 'string', 'string', 'string', 'string', 'string'),
(8, 'string', 'string', 'string', 'string', 'string', 'string', 'string', 'string', 'string', 'string', 'string', 'string', 'string', 'string', 'string', 'string', 'string', 'string', 'string'),
(9, 'string', 'string', 'string', 'string', 'string', 'string', 'string', 'string', 'string', 'string', 'string', 'string', 'string', 'string', 'string', 'string', 'string', 'string', 'string'),
(10, 'aaaaa', 'dddd', 'dddd', 'ddddd', 'aaaaaa', 'ffffff', 'gggggggg', 'sssssss', 'sssssssssssss', 'eeeeeeeeeeeee', 'rrrrrrrrrrrrrrrrrrrrr', 'rrrrrrrrrrrrrr', 'rrrrrrrrrrrrr', 'rrrrrrrrrrr', 'eeeeeeeeeeeeeeeeeeee', 'eeeeeeeeeeeeeeee', 'eeeeeeeeeeee', 'eeeeeeeeeeeeeee', 'wwwwwwwwwwwwwwwwwwwwwwww'),
(11, 'string', 'string', 'string', 'string', 'string', 'string', 'string', 'string', 'string', 'string', 'string', 'string', 'string', 'string', 'string', 'string', 'string', 'string', 'string'),
(12, 'string', 'string', 'string', 'string', 'string', 'string', 'string', 'string', 'string', 'string', 'string', 'string', 'string', 'string', 'string', 'string', 'string', 'string', 'string'),
(16, 'string', 'string', 'string', 'string', 'string', 'string', 'string', 'string', 'string', 'string', 'string', 'string', 'string', 'string', 'string', 'string', 'string', 'string', 'string'),
(17, 'string', 'string', 'string', 'string', 'string', 'string', 'string', 'string', 'string', 'string', 'string', 'string', 'string', 'string', 'string', 'string', 'string', 'string', 'string'),
(18, 'string', 'string', 'string', 'string', 'string', 'string', 'string', 'string', 'string', 'string', 'string', 'string', 'string', 'string', 'string', 'string', 'string', 'string', 'string'),
(19, 'aaaa', 'string', 'string', 'string', 'string', 'string', 'string', 'string', 'string', 'string', 'string', 'string', 'string', 'string', 'string', 'string', 'string', 'string', 'string'),
(20, 'aaaa', 'string', 'string', 'string', 'string', 'string', 'string', 'string', 'string', 'string', 'string', 'string', 'string', 'string', 'string', 'string', 'string', 'string', 'string'),
(21, 'aaaa', 'string', 'string', 'string', 'string', 'string', 'string', 'string', 'string', 'string', 'string', 'string', 'string', 'string', 'string', 'string', 'string', 'string', 'string');

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `okx_users`
--

CREATE TABLE `okx_users` (
  `id` int(11) NOT NULL,
  `api_key` varchar(255) NOT NULL,
  `secret_key` varchar(255) NOT NULL,
  `passphrase` varchar(255) NOT NULL,
  `total_balance` int(11) NOT NULL,
  `min_slot_play` int(11) NOT NULL,
  `status` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Đang đổ dữ liệu cho bảng `okx_users`
--

INSERT INTO `okx_users` (`id`, `api_key`, `secret_key`, `passphrase`, `total_balance`, `min_slot_play`, `status`) VALUES
(1, '3b906b00-776e-4ff0-8c30-738e97c8caab', '71FB64F6B47AAC190ECBB85D61B9A159', 'Tk115@utehy', 1111, 111, 1);

--
-- Chỉ mục cho các bảng đã đổ
--

--
-- Chỉ mục cho bảng `bot_alert`
--
ALTER TABLE `bot_alert`
  ADD PRIMARY KEY (`id`);

--
-- Chỉ mục cho bảng `okx_users`
--
ALTER TABLE `okx_users`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT cho các bảng đã đổ
--

--
-- AUTO_INCREMENT cho bảng `bot_alert`
--
ALTER TABLE `bot_alert`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- AUTO_INCREMENT cho bảng `okx_users`
--
ALTER TABLE `okx_users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
