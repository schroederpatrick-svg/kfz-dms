# KFZ-DMS für Raspberry Pi

Ein vollständiges Dokumenten-Management-System für KFZ-Werkstätten:

- Kundenverwaltung
- Fahrzeugverwaltung
- Auftragsmanagement
- Rechnungsmodul (inkl. ZUGFeRD/eRechnung)
- Artikel / Warenwirtschaft
- Automatische Backup & Restore Funktion
- Web-Frontend (Vue 3)
- FastAPI Backend
- PostgreSQL Datenbank
- Vollständig Dockerisiert
- Raspberry-Pi optimiert (ARMv7/v8)

---

## 🚀 Installation (One Command)

Lade das offizielle ZIP herunter (GitHub Release):

```bash
curl -L https://github.com/<user>/kfz-dms/releases/latest/download/kfz-dms.zip -o kfz-dms.zip
unzip kfz-dms.zip
cd kfz-dms
chmod +x install_kfz_dms_pi.sh
./install_kfz_dms_pi.sh
