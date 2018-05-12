from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np

coord_list = [
    ('new_york_city', 40.78, -73.98),
    ('bet_shemesh', 31.75, 34.99),
    ('tel_aviv', 32.07, 34.76),
    ('london', 51.51, -0.13),
    ('york', 53.96, -1.09),
    ('edinburgh', 55.95, -3.19),
    ('glasgow', 55.86, -4.25),
    ('belfast', 54.59, -5.93),
    ('pisa', 43.76, 10.38),
    ('florence', 43.77, 11.25),
    ('rome', 41.9, 12.50),
    ('johannesburg', -26.21, 28.05),
    ('mpaka', -26.43, 31.77),
    ('hluhluwe', -28.03, 32.28),
    ('cape_town', -33.93, 18.42),
    ('munich', 48.15, 11.58),
    ('zurich', 47.37, 8.55),
    ('paris', 48.86, 2.35),
    ('copenhagen', 55.67, 12.58),
    ('odense', 55.39, 10.39),
    ('malmo', 55.57, 13.11),
    ('vaxjo', 56.88, 14.81),
    ('stockholm', 59.33, 18.06),
    ('reykjavik', 64.13, -21.82),
    ('montreal', 45.50, -73.56),
    ('fort_lauderdale', 26.12, -80.14),
    ('san_jose', 9.93, -84.09),
    ('monteverde', 10.27, -84.83),
    ('la_fortuna', 10.47, -84.64),
    ('tortuguero', 10.54, -83.50),
    ('cahuita', 9.73, -82.84),
    ('manuel_antonio', 9.39, -84.14),
    ('paracas', -13.84, -76.25),
    ('nasca', -14.84, -74.93),
    ('puno', -15.84, -70.02),
    ('arequipa', -16.41, -71.54),
    ('cusco', -13.53, -71.97),
    ('abancay', -13.64, -72.89),
    ('andahuaylas', -13.66, -73.38),
    ('ayacucho', -13.16, -74.22),
    ('lima', -12.05, -77.04),
    ('santiago', -33.45, -70.67),
    ('canberra', -35.28, 149.13),
    ('sydney', -33.86, 151.21),
    ('uluru', -25.34, 131.03),
    ('melbourne', -37.8, 144.96),
    ('auckland', -36.84, 174.76),
    ('rotorua', -38.14, 176.25),
    ('whangarei', -35.73, 174.32),
    ('kerikeri', -35.23, 173.94),
    ('wellington', -41.29, 174.78),
    ('sukhothai', 17.01, 99.42),
    ('chiang_mai', 18.78, 99.00),
    ('bangkok', 13.76, 100.50),
    ('siem_reap', 13.36, 103.86),
    ('kratie', 12.49, 106.03),
    ('kampong_cham', 11.59, 105.27),
    ('krong_kep', 10.29, 104.19),
    ('phnom penh', 11.56, 104.93),
    ('singapore', 1.35, 103.82),
    ('hong_kong', 22.40, 114.11),
    ('tokyo', 35.69, 139.69),
    ('kyoto', 35.01, 135.77),
    ('nara', 34.68, 135.81),
    ('honolulu', 21.31, -157.86),
    ('kona', 19.64, -156.00),
    ('vancouver', 49.28, -123.12),
    ('washington_dc', 38.91, -77.04),
]

flight_list = [
    # Format (city, latitude, longitude)
    # We don't need to store the city names
    # They're included for readability and to make changes easier
    ('new_york_city', 40.78, -73.98),
    ('bet_shemesh', 31.75, 34.99),
    ('tel_aviv', 32.07, 34.76),
    ('london', 51.51, -0.13),
    ('london', 51.51, -0.13),
    ('pisa', 43.76, 10.38),
    ('rome', 41.9, 12.50),
    ('johannesburg', -26.21, 28.05),
    ('cape_town', -33.93, 18.42),
    ('munich', 48.15, 11.58),
    ('paris', 48.86, 2.35),
    ('copenhagen', 55.67, 12.58),
    ('stockholm', 59.33, 18.06),
    ('reykjavik', 64.13, -21.82),
    ('reykjavik', 64.13, -21.82),
    ('new_york_city', 40.78, -73.98),
    ('fort_lauderdale', 26.12, -80.14),
    ('san_jose', 9.93, -84.09),
    ('san_jose', 9.93, -84.09),
    ('lima', -12.05, -77.04),
    ('lima', -12.05, -77.04),
    ('santiago', -33.45, -70.67),
    ('santiago', -33.45, -70.67),
    ('sydney', -33.86, 151.21),
    ('sydney', -33.86, 151.21),
    ('uluru', -25.34, 131.03),
    ('uluru', -25.34, 131.03),
    ('melbourne', -37.8, 144.96),
    ('melbourne', -37.8, 144.96),
    ('auckland', -36.84, 174.76),
    ('auckland', -36.84, 174.76),
    ('bangkok', 13.76, 100.50),
    ('bangkok', 13.76, 100.50),
    ('siem_reap', 13.36, 103.86),
    ('phnom penh', 11.56, 104.93),
    ('singapore', 1.35, 103.82),
    ('singapore', 1.35, 103.82),
    ('hong_kong', 22.40, 114.11),
    ('hong_kong', 22.40, 114.11),
    ('tokyo', 35.69, 139.69),
    ('nara', 34.68, 135.81),
    ('honolulu', 21.31, -157.86),
    ('honolulu', 21.31, -157.86),
    ('vancouver', 49.28, -123.12),
    ('vancouver', 49.28, -123.12),
    ('washington_dc', 38.91, -77.04),
]

fig = plt.figure()
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])

m = Basemap(resolution=None,projection='robin', lon_0=0)

# Draw points representing cities
m.scatter([coords[2] for coords in coord_list], [coords[1] for coords in coord_list], 1, latlon=True, marker='o', color='cyan', zorder=10)

# Draw great circles representing flights
for start, end in zip(flight_list[0::2], flight_list[1::2]):
        m.drawgreatcircle(start[2], start[1], end[2], end[1], linewidth=0.5, color='ivory')

m.bluemarble(scale=0.5)
#m.drawcoastlines()
#m.fillcontinents()
# draw parallels
#m.drawparallels(np.arange(10,90,20),labels=[1,1,0,1])
# draw meridians
#m.drawmeridians(np.arange(-180,180,30),labels=[1,1,0,1],color='white')
ax.set_title('Where I Went')
plt.show()
