#### Trie

```java
package org.example;

import org.ahocorasick.trie.Emit;
import org.ahocorasick.trie.Trie;


import java.io.*;
import java.util.ArrayList;
import java.util.Collection;
import java.util.List;

public class Main {
    public static void main(String[] args)  {

        // 파일 객체 생성
        //File file = new File("D:\\workspace\\kowiki-20230701-all-titles-in-ns0");
        File file = new File("D:\\workspace\\slang.txt");

        // 파일 스트림 생성
        FileReader fileReader = null;
        try {
            fileReader = new FileReader(file);
        } catch (FileNotFoundException e) {
            throw new RuntimeException(e);
        }

        // 버퍼드 리더 생성
        BufferedReader bufferedReader = new BufferedReader(fileReader);

        // 파일 읽기
        String line;
        StringBuffer lines = new StringBuffer();
        Collection<String> aList = new ArrayList<>();
        while (true) {
            try {
                if (!((line = bufferedReader.readLine()) != null)) break;
            } catch (IOException e) {
                throw new RuntimeException(e);
            }
            // 파일 내용 출력
            //System.out.println(line);
            lines.append(line);

            aList.add(line);
        }

        // 파일 스트림 닫기
        try {
            fileReader.close();
        } catch (IOException e) {
            throw new RuntimeException(e);
        }

        //트라이에 단어 사전 생성
        Trie trie = Trie.builder().ignoreOverlaps()
                .addKeywords(aList)
                .build();



        // 문자열 검색
        String targetText = "어떤날 호랑이가 개같이 군다면 호랑나비인가 호랑개 또 그 무엇인가" ;
        StringBuffer convertText = new StringBuffer();

        Collection<Emit> emits = trie.parseText(targetText);

        int prevPos = 0;
        // 검색 결과 출력
        for (Emit emit : emits) {
            System.out.format("%s [%d : %d] \n", emit.getKeyword(), emit.getStart(), emit.getEnd());
            convertText.append(targetText.substring(prevPos, emit.getStart()));
            convertText.append(emit.getKeyword().replaceAll(".","*" ));
            prevPos = emit.getEnd() + 1;
        }

        convertText.append( targetText.substring( prevPos ) );
        System.out.println(convertText.toString());
    }
}

/**
slang.txt
호랑이
여우
개

실행결과 
호랑이 [4 : 6] 
개 [9 : 9] 
개 [26 : 26] 
어떤날 ***가 *같이 군다면 호랑나비인가 호랑* 또 그 무엇인가
**/

```
```xml
 <dependency>
            <groupId>org.ahocorasick</groupId>
            <artifactId>ahocorasick</artifactId>
            <version>0.4.0</version>
 </dependency>
```
