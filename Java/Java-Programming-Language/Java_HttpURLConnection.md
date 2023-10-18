#### HttpURLConnection
```java
        // URL을 지정합니다.
        URL url = new URL("https://api.example.com/users");

       // HttpURLConnection 객체를 생성합니다.
        HttpURLConnection connection  = null;
        connection  = (HttpURLConnection) url.openConnection();

       // HttpURLConnection 객체 속성을 설정합니다.        
        connection.setConnectTimeout(5000);    //서버에 연결되는 Timeout 시간 설정
        connection.setReadTimeout(5000);       //InputStream 읽어 오는 Timeout 시간 설정
        connection.setRequestProperty("Accept", "application/json");
        connection.setRequestProperty("Content-Type", "application/json");
        connection.setRequestProperty("appKey", "발급받은키");
        connection.setDoInput(true);
        connection.setDoOutput(true);
        connection.setRequestMethod("POST");    // 요청 메서드를 설정합니다.

       // Map을 생성합니다.
        Map<String, String> input = new HashMap<>();
        input.put("name", "John Doe");
        input.put("email", "johndoe@example.com");

        // ObjectMapper 객체를 생성합니다.
        ObjectMapper mapper = new ObjectMapper();

        // Map을 JSON으로 변환합니다.
        String requestBody = mapper.writeValueAsString(input);

        // 요청 본문을 설정합니다.
        OutputStreamWriter wr = new OutputStreamWriter(con.getOutputStream(), "UTF-8");
        wr.write(requestBody); //json 형식의 message 전달
        wr.flush();

        // 응답 코드를 읽습니다.
        int responseCode = connection.getResponseCode();

        // 응답 본문을 읽습니다.
       BufferedReader reader = new BufferedReader(new InputStreamReader(connection.getInputStream(), "UTF-8"));
       StringBuilder sb = new StringBuilder();
        String line;
        while ((line = reader.readLine()) != null) {
            sb.append(line);
        }
        reader.close();

      // 응담 코드에 따라 처리합니다.
      if (responseCode == HttpURLConnection.HTTP_OK) {
           System.out.println("" + sb.toString());
       } else {
          System.out.println("Response code: " + responseCode); 
       }




```
