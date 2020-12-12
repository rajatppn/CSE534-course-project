import time

from beacontools import BeaconScanner, IBeaconFilter, IBeaconAdvertisement

count = 0

def callback(bt_addr, rssi, packet, additional_info):
    print(packet.uuid, ",",rssi)
    # up_count()

# scan for all iBeacon advertisements from beacons with the specified uuid
# scanner = BeaconScanner(callback,
#     device_filter=[IBeaconFilter(uuid="fda50693-a4e2-4fb1-afcf-c6eb07647825")]
#
# )

# IBeaconFilter(uuid="fda50693-a4e2-4fb1-afcf-c6eb07647825"),
# IBeaconFilter(uuid="d546df97-4757-47ef-be09-3e2dcbdd0c77")
# IBeaconFilter(uuid="426c7565-4368-6172-6d42-6561636f6e73"),
# scanner.start()
# time.sleep(10)
# scanner.stop()

# # scan for all iBeacon advertisements regardless from which beacon
scanner1 = BeaconScanner(callback,
    packet_filter=IBeaconAdvertisement,
    device_filter=[
        IBeaconFilter(uuid="fda50693-a4e2-4fb1-afcf-c6eb07647825"),
        IBeaconFilter(uuid="d546df97-4757-47ef-be09-3e2dcbdd0c77"),
        IBeaconFilter(uuid="426c7565-4368-6172-6d42-6561636f6e73"),
        IBeaconFilter(uuid="526c7565-4368-6172-6d42-6561636f6e73"),
    ],
    scan_parameters={"interval_ms":100, "window_ms":90}
)
# scanner2 = BeaconScanner(callback,
#     packet_filter=IBeaconAdvertisement,
#     device_filter=[IBeaconFilter(uuid="d546df97-4757-47ef-be09-3e2dcbdd0c77")],
#     scan_parameters={"interval_ms":100, "window_ms":90}
# )
# scanner3 = BeaconScanner(callback,
#     packet_filter=IBeaconAdvertisement,
#     device_filter=[IBeaconFilter(uuid="426c7565-4368-6172-6d42-6561636f6e73")],
#     scan_parameters={"interval_ms":100, "window_ms":90}
# )
time.sleep(10)
print("Starting scan")
scanner1.start()
time.sleep(120)
scanner1.stop()
# scanner2.stop()
# scanner3.stop()
