```java
package com.test;

import java.util.ArrayList;
import java.util.List;

public class ExecTest {

	public static void main(String[] args) {

		List<User> userList = getUserList();

	//	simpleSort(userList, "ASC");

	//	simpleSort(userList, "DESC");

		insertSort(userList, "ASC");
		
		insertSort(userList, "DESC");
	}

	private static void simpleSort(List<User> userList, String sortType) {
		// asc
		if ("ASC".equals(sortType)) {
			for (int i = 0; i < userList.size(); i++) {
				for (int j = i + 1; j < userList.size(); j++) {
					if (userList.get(i).getScore() > userList.get(j).getScore()) {
						User tmp = userList.get(i);
						User tmp2 = userList.get(j);

						userList.set(i, tmp2);
						userList.set(j, tmp);
					}
				}

			}

		} else {
			// desc
			for (int i = 0; i < userList.size(); i++) {
				for (int j = i + 1; j < userList.size(); j++) {
					if (userList.get(i).getScore() < userList.get(j).getScore()) {
						User tmp = userList.get(i);
						User tmp2 = userList.get(j);

						userList.set(i, tmp2);
						userList.set(j, tmp);
					}
				}
			}

		}

		System.out.format("=========== UserList %s ==========\n", sortType);
		for (int i = 0; i < userList.size(); i++) {
			System.out.println(userList.get(i));
		}
	}

	public static void insertSort(List<User> userList, String sortType) {
		if ("ASC".equals(sortType)) {
			for (int i = 1; i < userList.size(); i++) {
				User current = userList.get(i);
				int j = i - 1;
	
				while (j >= 0 && userList.get(j).getScore() > current.getScore()) {
					userList.set(j + 1, userList.get(j));
					j--;
				}
	
				userList.set(j + 1, current);
			}
		} else {
			for (int i = 1; i < userList.size(); i++) {
				User current = userList.get(i);
				int j = i - 1;
	
				while (j >= 0 && userList.get(j).getScore() < current.getScore()) {
					userList.set(j + 1, userList.get(j));
					j--;
				}
	
				userList.set(j + 1, current);
			}
		}
		
		

		System.out.format("=========== UserList insertSort %s ==========\n", sortType);
		for (int i = 0; i < userList.size(); i++) {
			System.out.println(userList.get(i));
		}
	}

	public static List<User> getUserList() {
		List<User> userList = new ArrayList();

		User a = new User("Michael", 0.51);
		User b = new User("David", 0.0);
		User c = new User("John", 0.4932);
		User d = new User("Charles", 0.0839);
		User e = new User("Mary", 0.0712);
		User f = new User("Susan", 0.0014);

		userList.add(a);
		userList.add(b);
		userList.add(c);
		userList.add(d);
		userList.add(e);
		userList.add(f);

		return userList;
	}

	public static class User {

		public User(String name, Double score) {
			this.name = name;
			this.score = score;
		}

		private String name;
		private Double score;

		public String getName() {
			return name;
		}

		public void setName(String name) {
			this.name = name;
		}

		public Double getScore() {
			return score;
		}

		public void setScore(Double score) {
			this.score = score;
		}

		@Override
		public String toString() {
			return "User [name=" + name + ", score=" + score + "]";
		}

	}

}

```
