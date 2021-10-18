1. Higher Than 75 Marks
 - 문제의 해석 : substring, right, left, order by, where의 개념을 확인하기 위해 해당 데이터에서 이름을 출력하는 문제  
 - 선정한 이유 : 문제를 꼼꼼히 읽지 않으면 쉽게 틀릴 수 있고, 코테를 보는 경우 더욱 당황할 수 있는 있기에 선정하였습니다. 
 - 접근방식 : 처음 대충 읽고 풀었는데, 틀려서 마음을 차분히 하고 다시 천천히 읽고 풀었습니다. 
 - 코드 
  ```
  select name from students 
  where marks > 75 order by right(name, 3), id asc
  ```
 - 링크 : https://www.hackerrank.com/challenges/more-than-75-marks/problem?isFullScreen=true
  
2. Type of Triangle
 - 문제의 해석 : 삼각형의 각 변의 데이터가 1 컬럼씩 들어 있고 정삼각형인지, 이등변삼각형인지 삼격형의 종류를 구분하는 문제 
 - 선정한 이유 : case문 내에 case를 다시 사용할 수 있다는 점을 알리고 싶었고 새롭게 배운 내용이였기 때문입니다. 
 - 접근방식 : 먼저 삼각형이 성립하는지 여부를 판별하고 판별을 하였을 경우, 삼각형을 나누는 기준이 각 변의 길이가 같은지를 체크하는 식으로 코드를 구현해보았습니다. 
 - 코드 
  ```
  select 
  case when a+b>c and b+c>a and a+c>b then
          case when a=b and b=c then "Equilateral"
               when a=b or b=c or a=c then "Isosceles" else "Scalene" end
       else "Not A Triangle" end
  from triangles
  ```
 - 링크 : https://www.hackerrank.com/challenges/what-type-of-triangle/problem?isFullScreen=true
