```java
package org.springframework.samples.petclinic;
import java.lang.reflect.Field;
import java.lang.reflect.Method;
import java.lang.reflect.Parameter;
import java.lang.reflect.ParameterizedType;
import java.lang.reflect.Type;
import java.util.Iterator;
import java.util.Set;

import org.reflections.Reflections;
import org.reflections.scanners.SubTypesScanner;
/***************************************************
*   
    <dependency>
    <groupId>org.reflections</groupId>
    <artifactId>reflections</artifactId>
    <version>0.9.12</version>
   </dependency>
*
* package -> class -> methods -> method parameters 
****************************************************/
public class ShowClassInfos {

	public static void main(String[] args) throws ClassNotFoundException {
		// TODO Auto-generated method stub
		
		String packageName = "org.springframework.samples.petclinic.visit";
		String packageSimpleName = "petclinic";

		Reflections reflections = new Reflections(packageName, new SubTypesScanner(false)); 

		
		 Set<Class<? extends Object>> allClasses = 
		     reflections.getSubTypesOf(Object.class);
		 
		  for (Iterator<Class<? extends Object>> it = allClasses.iterator(); it.hasNext(); ) {
		        Object f = it.next(); //class
		        String fullName = f.toString();

		        String simpleClassName = fullName.substring(fullName.lastIndexOf('.') + 1);
		       
		        System.out.println("####################################################################") ;
		        System.out.println(simpleClassName) ;
		        
		        Class clazz = Class.forName(packageName+"."+simpleClassName);  //클래스 한개만 하고 싶으면 여기서 부터 
		        
		        Method methods[] = clazz.getDeclaredMethods();
		        int methodIdx = 0;
		        for (Method method : methods) {
		            System.out.println("===================================================================") ;       	
		            System.out.println("Get methods Name["+  ++methodIdx + "]" + method.getReturnType().getSimpleName()+" " + method.getName());

		   		    System.out.println("[IN params]") ;   
		            extractedInParams(packageSimpleName, method);
		            
		            
		            
		            Class<?> oparamClazz = null;
		            Type returnType = method.getGenericReturnType();
		            if(returnType instanceof ParameterizedType){
		            	  ParameterizedType type = (ParameterizedType) returnType;
		            	    Type[] typeArguments = type.getActualTypeArguments();
		            	    for(Type typeArgument : typeArguments){
		            	    	oparamClazz = (Class) typeArgument;
		            	        //System.out.println("typeArgClass = " + typeArgClass);
		            	       break;
		            	    }
		            }
		            
		            System.out.println("[OUT params]") ;     
		            if (oparamClazz == null) {
		            	oparamClazz = method.getReturnType();
		            	System.out.println(String.format("  %s:", oparamClazz.getSimpleName()));
		            }else {
		            	System.out.println(String.format(" %s<%s>:", method.getReturnType().getSimpleName(), oparamClazz.getSimpleName()));
		            }
		
		           
		           
		            Field[] ofields = extractedFields(oparamClazz);
		        }
		    }
		 
	}

	@SuppressWarnings("unused")
	private static void extractedInParams(String packageSimpleName, Method method) {    	
		Parameter[] parameters = method.getParameters();
		for (Parameter parameter : parameters) {
		   
			Class<?> paramClazz = null;
			
			 Type returnType = parameter.getParameterizedType();
			 if(returnType instanceof ParameterizedType){
           	    ParameterizedType type = (ParameterizedType) returnType;
           	    Type[] typeArguments = type.getActualTypeArguments();
           	    for(Type typeArgument : typeArguments){
           	    	paramClazz = (Class) typeArgument;
           	        //System.out.println("typeArgClass = " + typeArgClass);
           	       break;
           	    }
              }
			
			  
			  if (paramClazz == null) {
			     paramClazz = parameter.getType();  
			     System.out.println(String.format("  %s %s:", parameter.getType().getSimpleName(), parameter.getName()));
			   }else {
				 System.out.println(String.format(" %s<%s>:", parameter.getType().getSimpleName(), paramClazz.getSimpleName()));  
			   }
			   
			//   System.out.println("-- " + paramClazz.getName());
			   if (paramClazz.getName().indexOf(packageSimpleName) < 0) {
				   continue;
			   }
			   Field[] fields = extractedFields(paramClazz);
		    
		}
	}

	private static Field[] extractedFields(Class<?> paramClazz) {
		Field[] fields = paramClazz.getDeclaredFields();
		 //  System.out.println("-- " + paramClazz.getDeclaredFields().length);
		   for(Field field : fields) { 
			   field.setAccessible(true);
			
			
				System.out.println(String.format("    %s %s:", 
						field.getType().toString().substring(field.getType().toString().lastIndexOf('.') + 1), field.getName()));
		   }
		return fields;
	}
	
	

}


```
