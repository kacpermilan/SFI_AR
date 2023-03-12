using UnityEngine;

public class RotatingEarth : MonoBehaviour
{
    public GameObject rotationCenter;

    // Update is called once per frame
    void Update()
    {
        transform.RotateAround(rotationCenter.transform.position, Vector3.up, 20 * Time.deltaTime);
        transform.Rotate(new Vector3(0f, 50f, 0f) * Time.deltaTime);
    }
}
