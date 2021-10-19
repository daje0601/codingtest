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


3. Occupations
 - 문제의 해석 : 이름과 직업으로 구성된 컬럼을 직업 기준으로 재구성하는 문제입니다. 
 - 선정한 이유 : SQL에서 Pivot table을 만들 수 있는지를 체크하기 위해서 선정하였습니다. 
 - 접근방식 : RowNumber를 활용하여 각 그룹별 넘버링을 한 후 넘버링으로 group by 하여 풀었습니다. 
 - 코드 
  ```
  set @r1=0, @r2=0, @r3=0, @r4=0;
  select min(Doctor), min(Professor), min(Singer), min(Actor)
  from(
    select case when Occupation='Doctor' then (@r1:=@r1+1)
              when Occupation='Professor' then (@r2:=@r2+1)
              when Occupation='Singer' then (@r3:=@r3+1)
              when Occupation='Actor' then (@r4:=@r4+1) end as RowNumber,
      case when Occupation='Doctor' then Name end as Doctor,
      case when Occupation='Professor' then Name end as Professor,
      case when Occupation='Singer' then Name end as Singer,
      case when Occupation='Actor' then Name end as Actor
    from OCCUPATIONS
    order by Name
   ) temp
  group by RowNumber;
  ```
  - 링크 : https://www.hackerrank.com/challenges/occupations/problem  


4. Occupations
 - 문제의 해석 : 트리 노드 정보를 담고 있는 테이블에서 각각의 row가 어디에 해당하는지를 가려내는 문제입니다. 
 - 선정한 이유 : 트리에 대한 이해와 SQL조건문을 다룰 수 있는지를 확인 할 수 있는 문제여서 선정하였습니다. 
 - 접근방식 : P에 null이 있다면 그것은 루트노드로 간주 할 수 있고, n에 있는 값이 P 있다면 inner 노드라고 간주할 수 있다는 아이디어로 접근하였습니다. 
 - 코드 
  ```
  select 
  case when P is null then concat(N, ' Root')
     when N in (select distinct P from bst) then concat(N, ' Inner')
     else concat(N, ' Leaf') end
  from bst
  ORDER BY N ASC
  ```
 - 링크 : https://www.hackerrank.com/challenges/binary-search-tree-1/problem 
