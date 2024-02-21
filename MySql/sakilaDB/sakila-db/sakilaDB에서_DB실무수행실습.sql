USE sakila;
desc actor;
SHOW DATABASES;
SHOW TABLES;

#1번문제 영화 테이블(film) 에서 총 영화 수
SELECT * FROM film;
SELECT COUNT(*) FROM film;

# 2번문제 영화 등급종류 추출 (rating)
SELECT DISTINCT rating FROM film;

#3번문제 영화 테이블(film) 에서 영화 release 연도 종류 알아내기, 각 영화의 release 연도는 release_year 컬럼에 있음
SELECT DISTINCT release_year FROM film LIMIT 10;

#4번 영화 렌탈 테이블(rental) 에서 10개 데이터만 출력하기, rental 테이블은 (DVD 를 언제, 누가 빌려갔고, 반환했는지에 대한 정보)
SELECT * FROM rental;
SELECT * FROM rental LIMIT 10;

#5번 영화 렌탈 테이블(rental) 에서 inventory_id 가 367 인 로우(Row) 전체 출력하기
SELECT * FROM rental WHERE inventory_id=367;

#6번  customer 테이블에서 customer 수 알아내기
SELECT COUNT(*) FROM customer;

#7번 payment 테이블에서 렌탈비용 합계, 평균, 최대값, 최소값 구하기, payment 테이블은 렌탈 비용을 포함한 정보를 담고있는 테이블임
SELECT * FROM payment; 
SELECT SUM(amount) FROM payment; #합계;
SELECT AVG(amount) FROM payment; #평균;
SELECT MAX(amount) FROM payment; #최대값;
SELECT MIN(amount) FROM payment; #최소값;

#8번 영화 렌탈 테이블(rental) 에서 inventory_id 가 367 이고, staff_id가 1인 로우(Row) 전체 출력하기
SELECT * FROM rental;
SELECT * FROM rental WHERE inventory_id=367 AND staff_id=1;

#10번  영화(film table)에 매겨진 등급(rating) 종류에 따른 영화 갯수를 모두 출력하시요 (rating 값과 각 rating 값에 따른 영화 갯수를 출력하세요(중요)
SELECT * FROM film;
SELECT rating, SUM(rating) FROM film GROUP BY rating;

#11번 영화(film table)에서 영화가 PG 또는 G 등급의 영화 수를 각 등급별로 출력하세요 (rating 값과 각 rating 값에 따른 영화 갯수를 출력하세요)
SELECT * FROM film;
SELECT rating, COUNT(*) FROM film WHERE rating='G' OR rating='PG' GROUP BY rating;

#12번 영화(film table)에서 영화가 G 등급인 영화 제목을 출력하세요
SELECT title FROM film WHERE rating='G';

#13번 영화(film table)에서 영화가 PG 또는 G 등급인 영화 제목을 출력하세요
SELECT title,rating FROM film WHERE rating='G' OR rating='PG';

#14번 영화(film table)에서 release 연도가 2006 또는 2007 연도이고, 영화가 PG 또는 G 등급인 영화 제목을 출력하세요
SELECT title,rating,release_year FROM film WHERE (release_year=2006 OR release_year=2007) AND (rating='G' OR rating='PG');

#15,16번 film테이블에서 rating (등급)으로 그룹을 묶어서, 각 등급별 영화 갯수 출력하기 (각 등급별 갯수 출력하기)
SELECT rating,COUNT(*) FROM film GROUP BY rating;

#17번  film테이블에서 rating (등급)으로 그룹을 묶어서, 각 등급별 영화 갯수와 각 등급별 평균 렌탈 비용 출력하기 (등급과 각등급별 갯수, 각 등급별 평균 렌탈 비용 출력하기)
SELECT rating,COUNT(*),AVG(rental_duration) FROM film GROUP BY rating;

#18번  film테이블에서 rating (등급)으로 그룹을 묶어서, 각 등급별 영화 갯수와 각 등급별 평균 렌탈 비용 출력하기, 단 평균 렌탈비용이 높은 순으로 출력하기 (등급과 각 등급별 갯수, 각 등급별 평균 렌탈 비용 출력하기)
SELECT rating, COUNT(*), AVG(rental_duration) FROM film  GROUP BY rating ORDER BY AVG(rental_duration) DESC;

#19,20번 film테이블에서 rating (등급)으로 그룹을 묶어서, 각 등급별 영화 갯수와 rating (등급), 각 그룹별 평균 rental_rate (렌탈 비용) 출력하되, 영화 갯수와 평균 렌탈 비용은 각각 total_films, avg_rental_rate 으로 출력하고, avg_rental_rate이 높은 순으로 출력하시오 (SQL 구문을 보기 좋게 여러 줄에 걸쳐서 써보기)
 SELECT rating, COUNT(*) AS total_films, FLOOR(AVG(rental_rate)) AS avg_rental_rate FROM film GROUP BY rating ORDER BY FLOOR(AVG(rental_rate)) DESC