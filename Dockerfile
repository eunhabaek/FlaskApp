FROM python:3.8-slim

RUN apt-get update

#필요한 패키지들 설치 (대화형 작업은 못 하므로 -y 필수)
RUN apt-get install -y --no-install-recommends

#작업 디렉토리 만들기
WORKDIR /usr/src/app

#필요한 파일 복사
COPY requirements.txt ./

RUN pip install -r requirements.txt

#소스 파일 모두 복사
COPY . .

#포트 열어주기(app.py에서 확인 가능)
EXPOSE 5000

#명령어
CMD ["python","-m","flask","run","--host=0.0.0.0"]