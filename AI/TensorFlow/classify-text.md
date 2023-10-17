#### TensorFlow Lite Model Maker를 사용하여 커스텀 텍스트 분류 모델 만들기
참고 : 
 - https://developers.google.com/codelabs/classify-text-update-tensorflow-serving?hl=ko#0
 - https://www.tensorflow.org/lite/api_docs/python/tflite_model_maker/text_classifier

개발환경 : <br><br>
[ 모델 생성 환경 ]
  - python 
    python-3.12.0-amd64.exe -> python-3.9.6-amd64.exe (version downgrade , TensorFlow Lite가 python 최신 버전에서 안됨)
    https://www.tensorflow.org/install?hl=ko
    만약 뭐가 안되서 에러날때는 해당 패키지 version downgrade 시도
  - IDE <br>
    VSCode
  - 학습데이터 <br>
    예제로 나온 경로는 에러가 발생하여 다른 파일로 대체

[ API 환경 ]
 - Flutter SDK
 - Android
 - Docker

```docker
docker run -it --rm -p 8500:8500 -p 8501:8501 -v "D:\mm_spam_savedmodel\saved_model:/models/spam-detection/1/" -e MODEL_NAME=spam-detection tensorflow/serving
```
