# AVP Mapping and Localization
This is a visual mapping and localization project construct for autonomous valet parking task based on Baidu Apollo Framework. Contains the following modules.

- Mapping: running offboard  
1. **dumper**: convert raw trip data into proto messages  
2. **visual odometry**: compute relative poses between frames
3. **feature extractor**: extract features used in parking task
4. **mapping pipeline**: build a consistent map of multi trips  

- Localization: running onboard
1. **graph based localization**: multi sensors fusion localization
2. **visual place recognition**: visual relocalization