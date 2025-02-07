import org.json.JSONArray;
import org.json.JSONObject;

public class JsonArrayExample {
    public static void main(String[] args) {
        String jsonString = "{\"students\": [\"Alice\", \"Bob\", \"Charlie\"]}";
        JSONObject json = new JSONObject(jsonString);
        JSONArray students = json.getJSONArray("students");

        for (int i = 0; i < students.length(); i++) {
            System.out.println(students.getString(i));
        }
    }
}
