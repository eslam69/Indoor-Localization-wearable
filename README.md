# Indoor-Localization-Wearable
This project was developed for educational purposes as a project work in sbe403a Medical Electronics Systems(SBME department, faculty of engineering, Cairo University).

The system was tested on a single floor at the SBME department in Cairo university's campus.
## Methodology
The used approach in the development of this system was based on WIFI fingerprints by this was done by collecting WIFI-RSSI data(Received signal strength indication) at different locations to train and select the best machine learning model that can be used to classify or predict the location of an esp32-based wearable device according to the latest RSSI sent from the device to a real time database (firebase). 
![system diagram](/resources/localizer_diagram.png)

### Clients:
* **Mobile APP:**
 
![QT GUI](/resources/mobile_gif.gif)

* **Desktop APP:**
 
![QT GUI](/resources/guiSnap.png)
