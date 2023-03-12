using UnityEngine;

public class RotatingCapibara : MonoBehaviour
{
    // Update is called once per frame
    void Update()
    {
        transform.Rotate(new Vector3(0f, 0f, 50f) * Time.deltaTime);
    }
}
