import org.json.JSONObject;

public class JsonToJava {
    public static void main(String[] args) {
        String jsonString = "{\"name\":\"Coffee33\", \"age\":26, \"city\":\"Berlin\"}";
        JSONObject json = new JSONObject(jsonString);

        String name = json.getString("name");
        int age = json.getInt("age");
        String city = json.getString("city");

        System.out.println("Name: " + name);
        System.out.println("Age: " + age);
        System.out.println("City: " + city);
    }
}
