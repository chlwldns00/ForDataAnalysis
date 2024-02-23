CREATE DATABASE bestproducts;
USE bestproducts;
desc ranking;
SELECT * FROM ranking;
SELECT * FROM items;

#1번 전체 베스트상품(ALL 메인 카테고리)에서 판매자별 베스트상품 갯수 높은순으로 출력
SELECT provider, COUNT(*) AS best_product_num FROM ranking r INNER JOIN items i ON r.item_code=i.item_code WHERE r.main_category='ALL' GROUP BY provider ORDER BY COUNT(*) DESC;

#2번 메인 카테고리가 패션의류인 (서브 카테고리 포함), 패션의류 전체 베스트상품에서 판매자별 베스트 상품 갯수가 5이상인 판매자와 베스트상품 갯수 출력해보기
SELECT provider, COUNT(*) AS best_product_num FROM ranking r INNER JOIN items i ON r.item_code=i.item_code WHERE r.main_category="패션의류" GROUP BY provider HAVING COUNT(*)>=5;

#3번 sakila 데이터베이스에서 address 테이블에는 address_id 가 있지만, customer 테이블에는없는 데이터의 갯수 출력하기
USE sakila;
SELECT * FROM address;
SELECT * FROM customer;
SELECT COUNT(*) AS none FROM customer c RIGHT OUTER JOIN address a ON c.address_id=a.address_id WHERE customer_id IS NULL;

#4번 메인 카테고리별로 할인 가격이 10만원 이상인 상품이 몇개 있는지를 출력해보기 (JOIN 활용 SQL 과 서브쿼리 활용 SQL 모두 작성해보기
SELECT main_category, COUNT(*) AS 10만원넘는상품 FROM items i JOIN ranking r ON i.item_code=r.item_code WHERE i.dis_price>=100000 GROUP BY r.main_category;

#****** 5번 items' 테이블에서 'dis_price'가 200000 이상인 아이템들 중, 각 'sub_category'별 아이템 수를 구하시오. 이때 서브쿼리를 사용하시오 
SELECT r.sub_category, COUNT(*) FROM ranking r WHERE r.item_code IN (SELECT i.item_code FROM items i WHERE i.dis_price>=200000)  GROUP BY r.sub_category;

#******6번 메인 카테고리, 서브 카테고리에 대해, 평균할인가격과 평균할인율을 출력해보기(group by AB)
SELECT main_category, sub_category, AVG(dis_price), AVG(discount_percent) FROM items JOIN ranking ON items.item_code=ranking.item_code GROUP BY main_category, sub_category;

#7번 판매자별 베스트상품 갯수, 평균할인가격, 평균할인율을 베스트상품 갯수가 높은 순으로 출력
SELECT provider, COUNT(*), AVG(dis_price), AVG(discount_percent) FROM items JOIN ranking ON items.item_code=ranking.item_code GROUP BY provider ORDER BY COUNT(*) DESC;

# *** 8번 각 메인 카테고리에서 베스트 상품 갯수가 20개 이상인 판매자의 판매자별 평균할인가격, 평균할인율, 베스트 상품 갯수 출력해보기
SELECT r.main_category, i.provider, COUNT(*), AVG(dis_price), AVG(discount_percent) FROM items i JOIN ranking r ON i.item_code=r.item_code GROUP BY provider HAVING COUNT(*)>=20 ORDER BY COUNT(*) DESC;

#9번 'items' 테이블에서 'dis_price'가 50000 이상인 상품들 중, 각 'main_category'별 평균'dis_price'와 'discount_percent' 출력해보기
SELECT r.main_category, AVG(dis_price), AVG(discount_percent) FROM items i JOIN ranking r ON i.item_code=r.item_code WHERE i.dis_price>=50000  GROUP BY r.main_category;