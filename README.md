# 2018-2 객체지향 프로그래밍 프로젝트 - **{조명(Light)}**
구성원: 2-5 지명금 | 2-6 유현아 | 2-6 이준홍

## 1. 주제  
셀프 인테리어 도우미(부제: 너가 사는 그 집)  

## 2. 동기
  최근 들어 데이터를 이용하여 패션, 음식등 다양한 쇼핑 정보를 제공하는 사이트들이 등장하고 있다. 인테리어 업체가 아닌 개인적으로 셀프 인테리어를 하는 사람들이 증가하고 있다. 이러한 사회 동향에 따라, 사용자가 원하는 정보를 입력하면  사용자가 사는 집의 정보나 취향에 따라 가구나 벽지등의 인테리어 제품을 제공해주는 사이트가 필요하다고 생각했다.


## 3. 프로그램 사용 대상
인테리어를 하고 싶어 하지만,  
*1) 인테리어에 대한 정보가 부족하고*  
*2) 인테리어 제품 구매에 대한 정보가 부족하여*  

누군가의 도움이 필요한 사람들  

## 4. 목적
인테리어에 무지한 사람들이 자신이 원하는 테마의 가구들을 사게 함으로써 쉽게 인테리어를 하도록 도와줄 수 있다.  

## 5. 주요기능  
#### 1) 제품 출처 선택
  - (옥션 / 11번가 등.. )프로그램에서 데이터의 출처로 사용할 사이트를 사용자가 선택    
  
#### 2) 사용자 조건 입력  
1. 방의 크기 선택 : 
- ‘원룸’ 혹은 ‘투룸 이상’을 선택한다. (가구 사이즈 분류를 위함)  
  
2. 테마 선택 : 
- 사용자가 찾고 싶은 상품의 테마를 선택한다.  
( ex: ‘차분한’ / ‘발랄한’ 등의 테마로 정리해서 제공해준다 )  
( 사진->색상 테마 추출->색상테마를 ‘차분한’,‘발랄한’등의 테마로 정리->사용자가 테마를 선택->제품들중 색상테마에 속한 색상의 제품을 정리 )  

3. 구체적인 제퓸 유형 선택 :  
- 인테리어 제품의 유형(침대, 서랍장)을 정리해서 사용자가 선택할 수 있게 함    

#### 3) 제품 정보 제공
- 사용자가 선택한 제품 조건에 맞는 제품을 가격이 저렴한 순서대로 제공해줌  
- 사용자가 관심있는 상품을 선택하면 관심상품을 별도로 모아둠  

## 6. 프로젝트 핵심
사용자가 원하는 테마에 따라 인테리어 제품을 소개시켜주고, 프로그램 내에서 사용자가 선택한 관심상품을 모아준다.  

## 7. 구현에 필요한 라이브러리나 기술
#### 1) 필요한 라이브러리
- [pyqt5](https://pypi.org/project/PyQt5/) :: GUI 구성을 마우스로 할 수 있는 프로그램을 제공  
- [Selenium](https://www.seleniumhq.org/) :: 웹파싱에 이용  
- [beautifulsoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) :: 웹파싱에 이용  
- [OpenCV-Python](https://opencv.org/) :: 이미지 처리에 이용  
#### 2) 구현에 필요한 기술
- 사진을 사이트에 업로드 하여 사진 속에 사용된 컬러의 색상 값을 파싱해오는 기술  
- 사용자가 입력한 조건에 맞추어서 인테리어 제품을 파싱해오는 기술  
- 프로그램 내에서 자유롭게 제품을 둘러보고 선택하게 하는 기술  


## 8. **분업 계획**
1) 인테리어 데이터셋 제작 : **지명금**  
  - 테마에 따른 컬러차트(색상표 데이터)  
  - 인테리어 제품의 사진, 규격, 테마, 색상정보 데이터  
  
2) 사용자 상호작용 (조건 입력 데이터 제공) : **유현아**    
  - 사용자가 입력받은 데이터에 맞추어서 파싱된 데이터 제공  
  - 사용자가 선택한 관심상품을 별도로 모은다  
  
3) GUI 제작 : **이준홍(80%) , 지명금(10%), 유현아(10%)**    

## 9. 프로젝트에서 사용하는 사이트  
#### 1) 컬러 테마를 만들기 위한 사이트
  1) [인테리어 테마와 사진을 제공하는 사이트(1)](https://www.homify.co.kr/rooms/living-room)
  2) [인테리어 테마와 사진을 제공하는 사이트(2)](https://ohou.se/)
  3) [사진에서 컬러정보를 뽑아오는 사이트](http://www.colr.org/)

#### 2) 인테리어 제품 사이트
  1) [텐바이텐](http://www.10x10.co.kr/shopping/category_list.asp?disp=121102104)
  2) [이케아](https://www.ikea.com/)
  3) [리모드](http://www.remod.co.kr/)
  4) [디자인 스페이스](http://www.gagu824.com/shop/main/index.php)
  5) [두닷](https://www.dodot.co.kr/)
  6) [까유](http://www.kayumall.com/)
  7) [무인양품](http://www.muji.com/kr/)
  8) [마켓엠](http://www.market-m.co.kr/)
  9) [인디테일](http://www.indetail.co.kr/shop/main/index.php)
  10) [필웰](http://www.feelwell.co.kr/)
  
  배경없는 사이트
  1) [이케아](https://www.ikea.com/)
  2) [리모드](http://www.remod.co.kr/)
  3) [인디테일](http://www.indetail.co.kr/shop/main/index.php) :: 소파제외 사용가능 
  4) [자주JAJU](http://living.sivillage.com/jaju/display/displayShop?temp=www.jaju.co.kr) -> ajax 필요함  
  5) [모던하우스](http://modernhouse.elandmall.com/main/initMain.action) :: 침구제외 사용 가능
