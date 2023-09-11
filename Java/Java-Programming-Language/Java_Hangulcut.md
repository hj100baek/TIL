```java
//한글 자르기

 public static String subStrBytes(String source, int cutLength, String charSet) {
			if(!source.isEmpty()) {
		    	source = source.trim();
      try {
					if(source.getBytes(charSet).length <= cutLength) {
						return source;
					} else {
					    StringBuffer sb = new StringBuffer(cutLength);
					    int cnt = 0;
					    for(char ch : source.toCharArray()){
					    	cnt += String.valueOf(ch).getBytes(charSet).length;
					        if(cnt > cutLength) 
					        	break;
					        sb.append(ch);
					    }
					    return sb.toString();
					}
				} catch (UnsupportedEncodingException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
		    } else {
		    	return "";
		    }
			return "";
		}

```
