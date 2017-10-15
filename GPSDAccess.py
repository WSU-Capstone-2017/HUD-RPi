import gps

#Listen on gpsd of local host
session = gps.gps("localhost","2947")
session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)

while True:
    try:
        report = session.next()
        if report['class'] == 'TPV':
            if hasattr(report, 'time'):
                print report.time
    except KeyError:
        pass
    except KeyboardInterrupt:
        quit()
    except StopIteration:
        session = None
        print "GPSD has terminated"
