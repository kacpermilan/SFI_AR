using System.Collections.Generic;
using UnityEngine;
using UnityEngine.XR.ARFoundation;

[RequireComponent(typeof(ARTrackedImageManager))]
public class PlaceTrackedImages : MonoBehaviour
{
    private ARTrackedImageManager _imageManager;
    private readonly Dictionary<string, GameObject> _createdPrefabs = new();

    public GameObject[] ARPrefabs;

    // Store the reference to the application Tracked Image Manager.
    private void Awake()
    {
        _imageManager = GetComponent<ARTrackedImageManager>();
    }

    // Subscribe to react on changes in tracked images with appropriate handler.
    private void OnEnable()
    {
        _imageManager.trackedImagesChanged += OnTrackedImagesChanged;
    }

    // Unsubscribe from the change in tracked images event.
    private void OnDisable()
    {
        _imageManager.trackedImagesChanged += OnTrackedImagesChanged;
    }

    // Handle the obtained information about the change (update, add, remove) in tracked images.
    private void OnTrackedImagesChanged(ARTrackedImagesChangedEventArgs changeContext)
    {
        // Update the state of all existing prefabs
        foreach (ARTrackedImage image in changeContext.updated)
        {
            _createdPrefabs[image.referenceImage.name].SetActive(image.trackingState == UnityEngine.XR.ARSubsystems.TrackingState.Tracking);
        }

        // Acknowledge the reckognition of new image and create an associated prefab
        foreach (ARTrackedImage image in changeContext.added)
        {
            string imageName = image.referenceImage.name;

            foreach(GameObject prefab in ARPrefabs)
            {
                // Name based corelation, prefabs must have identical names as the images
                if (prefab.name.Equals(imageName) && !_createdPrefabs.ContainsKey(imageName))
                {
                    GameObject newPrefab = Instantiate(prefab, image.transform);
                    _createdPrefabs.Add(imageName, newPrefab);
                }
            }
        }

        // Remove the prefab, when associated image can no logner be tracked
        foreach (ARTrackedImage image in changeContext.removed)
        {
            Destroy(_createdPrefabs[image.referenceImage.name]);
            _createdPrefabs.Remove(image.referenceImage.name);
        }
    }
}
