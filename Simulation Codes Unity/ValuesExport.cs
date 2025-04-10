using System.IO;
using UnityEngine;

public class ValuesExport : MonoBehaviour
{
    private StreamWriter writer;
    private string filePath;
    private int frameCount = 0;

    void Start()
    {
        // Create a timestamped filename
        string timestamp = System.DateTime.Now.ToString("yyyyMMdd_HHmmss");
        filePath = Path.Combine(Application.persistentDataPath, $"float_data_{timestamp}.csv");

        // Initialize CSV file with header
        writer = new StreamWriter(filePath);
        writer.WriteLine("Frame,Timestamp,Value");
        writer.Flush(); // Write immediately to file

        Debug.Log($"Logging float values to: {filePath}");
    }

    // Call this whenever you calculate a new float value
    public void LogFloatValue(float value)
    {
        string timestamp = System.DateTime.Now.ToString("HH:mm:ss.fff");
        writer.WriteLine($"{frameCount},{timestamp},{value.ToString()}");
        writer.Flush(); // Ensure data is written immediately
        frameCount++;
    }

    void OnDestroy()
    {
        if (writer != null)
        {
            writer.Close();
            Debug.Log($"Finished logging. File saved to: {filePath}");
        }
    }
}