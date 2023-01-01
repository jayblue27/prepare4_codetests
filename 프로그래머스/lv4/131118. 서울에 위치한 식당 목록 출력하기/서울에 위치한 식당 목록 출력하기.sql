-- 코드를 입력하세요
-- 리뷰 평균 점수 - AVG 소수점 3자리 반올림
-- 서울에 위치한 식당 - WHERE
-- 평균점수 내림차순 - ORDER BY
-- 즐겨찾기수 내림차순 

SELECT 
    REST_ID,
    REST_NAME,
    FOOD_TYPE,
    FAVORITES,
    ADDRESS,
    ROUND(AVG(REVIEW_SCORE), 2) AS SCORE
FROM REST_REVIEW
LEFT JOIN REST_INFO
USING(REST_ID)
WHERE ADDRESS REGEXP '^서울'
GROUP BY REST_ID
ORDER BY 
    SCORE DESC, 
    FAVORITES DESC