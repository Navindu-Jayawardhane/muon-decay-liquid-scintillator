using UnityEngine;

public class MuonFall : MonoBehaviour
{
    void Start()
    {
        Rigidbody rb = GetComponent<Rigidbody>();
        rb.linearVelocity = new Vector3(0, -5f, 0); // New preferred way
    }
}
