#!/usr/bin/env python3
"""Structured entries parsed from HUD行人碰撞预警_风险时机判断_论文清单.md (list 2)."""

REFS2 = [
    dict(key="kang2016ttc", doi="10.24230/kjiop.v29i2.257-277", year=2016,
         title="Differences in Drivers' Pedestrian Avoidance Response Based on Warning Timing, Stimulus-Response Compatibility and Drivers' Distraction",
         authors="Kang, Han, Lee", group="预警时机"),
    dict(key="lubbe2017", doi="10.1016/j.jsr.2017.02.002", year=2017,
         title="Brake reactions of distracted drivers to pedestrian Forward Collision Warning systems",
         authors="Lubbe", group="预警时机"),
    dict(key="zhangyt2015", doi="10.1109/ictis.2015.7232174", year=2015,
         title="Effects of collision warning system under different warning timing on driving speed and distance",
         authors="Zhang, Li, Yan, Xue", group="预警时机"),
    dict(key="chenyl2013fcw", doi="10.1109/iciea.2013.6566508", year=2013,
         title="Forward collision warning system considering both time-to-collision and safety braking distance",
         authors="Chen, Shen, Wang", group="预警时机"),
    dict(key="attc2025", doi="10.2139/ssrn.6351998", year=2025,
         title="A-TTC: A Multimodal Fusion Framework for Personalized Truck Forward Collision Warning via Dynamic Threshold Calibration",
         authors="Wang, He, Guo, Stevenson, Xu", group="预警时机"),
    dict(key="abe2006", doi="10.1016/j.apergo.2005.11.001", year=2006,
         title="Alarm timing, trust and driver expectation for forward collision warning systems",
         authors="Abe, Richardson", group="预警时机"),
    dict(key="abe2004", doi="10.1037/e577202012-006", year=2004,
         title="The human factors of collision warning systems: system performance, alarm timing, and driver trust",
         authors="Abe, Richardson", group="预警时机"),
    dict(key="thammakaroon2012", doi="10.1109/icves.2012.6294314", year=2012,
         title="Improvement of warning lag time in forward collision warning system based on multifunctional warnings",
         authors="Thammakaroon, Tangamchit", group="预警时机"),
    dict(key="lind2007cwhud", doi="10.4271/2007-01-1105", year=2007,
         title="An Efficient Visual Forward Collision Warning Display for Vehicles",
         authors="Lind", group="HUD显示"),
    dict(key="kim2018tvcg", doi="10.1109/tvcg.2018.2793680", year=2018,
         title="Driver Behavior and Performance with Augmented Reality Pedestrian Collision Warning: An Outdoor User Study",
         authors="Kim, Gabbard, Anon, Misu", group="HUD显示"),
    dict(key="kim2016shadow", doi="10.1109/vr.2016.7504725", year=2016,
         title="Casting shadows: Ecological interface design for augmented reality pedestrian collision warning",
         authors="Kim, Isleib, Gabbard", group="HUD显示"),
    dict(key="large2018urgency", doi="10.1016/j.trf.2018.09.028", year=2018,
         title="Investigating the effect of urgency and modality of pedestrian alert warnings on driver acceptance and performance",
         authors="Large, Kim, Merenda, Leong, Harvey, Burnett, Gabbard", group="HUD显示"),
    dict(key="bao2024crowd", doi="10.12677/ap.2024.148539", year=2024,
         title="Effects of Visual Crowding and Stimulus Location on Driver Pedestrian Perception in AR-HUD Warning",
         authors="鲍威宇", group="HUD显示"),
    dict(key="ye2025plane2", doi="10.3390/electronics14234768", year=2025,
         title="Spatial Plane Positioning of AR-HUD Graphics: Implications for Driver Inattentional Blindness in Navigation and Collision Warning Scenarios",
         authors="Ye, Yin", group="HUD显示"),
    dict(key="shen2023flash", doi="10.54941/ahfe1008065", year=2023,
         title="Effect of AR-HUD Warning Information Presentation Modes on Driver Situation Awareness under Single-Hazard Scenarios",
         authors="Shen, Qin, Li, Shi, Zou, Ran", group="HUD显示"),
    dict(key="phan_thesis", doi="", year=2016,
         title="Estimation of driver awareness of pedestrian for an Augmented Reality advanced driving assistance system",
         authors="Phan", group="HUD显示",
         url="https://theses.hal.science/tel-01466680"),
    dict(key="schall_thesis", doi="10.17077/etd.tbjq72y2", year=2013,
         title="Augmented reality cues and elderly driver hazard perception",
         authors="Schall", group="HUD显示",
         url="https://iro.uiowa.edu/esploro/outputs/doctoral/9983777005002771"),
    dict(key="maroto2018hud", doi="", year=2018, arxiv="1803.08383",
         title="Head-up Displays (HUD) in driving",
         authors="Maroto, Caño, González, Villegas", group="HUD显示"),
    dict(key="char_thesis", doi="", year=2022,
         title="Pedestrian and cyclist forward collision warning system effectiveness estimation based on simulation of kinematic reconstructions",
         authors="Char", group="算法系统",
         url="https://theses.hal.science/tel-04028593"),
    dict(key="chang2013bus", doi="10.4018/978-1-4666-2649-2.ch011", year=2013,
         title="The Development of Parameters and Warning Algorithms for an Intersection Bus-Pedestrian Collision Warning System",
         authors="Chang, Chang", group="算法系统"),
    dict(key="chang2009apscc", doi="10.1109/apscc.2009.5394118", year=2009,
         title="Parameters Analysis for an Intersection Bus-Pedestrian Collision Warning System",
         authors="Chang, Chang", group="算法系统"),
    dict(key="jung2016cnn", doi="", year=2016, arxiv="1612.06558",
         title="End-to-End Pedestrian Collision Warning System based on a Convolutional Neural Network with Semantic Segmentation",
         authors="Jung, Choi, Soon, Jung", group="算法系统"),
    dict(key="cangut2026intent", doi="10.5592/co/cetra.2026.1849", year=2026,
         title="Machine learning-based pedestrian intention prediction models for collision warning at unsignalized crosswalks",
         authors="Cangut, Alver", group="算法系统"),
    dict(key="banerjee2021pcw", doi="", year=2021, arxiv="2112.09074",
         title="Influence of Pedestrian Collision Warning Systems on Driver Behavior: A Driving Simulator Study",
         authors="Banerjee, Jihani, Khadel, Kabir", group="算法系统"),
    dict(key="certad2025v2p", doi="", year=2025, arxiv="2504.13906",
         title="V2P Collision Warnings for Distracted Pedestrians: A Comparative Study with Traditional Auditory Alerts",
         authors="Certad, Del Re, Varughese, Olaverri-Monreal", group="算法系统"),
    dict(key="wolf2021early", doi="", year=2021, arxiv="2107.05186",
         title="Early warning of pedestrians and cyclists",
         authors="Wolf", group="算法系统"),
    dict(key="suzuki2010fusion", doi="10.1109/ivs.2010.5548120", year=2010,
         title="Sensor fusion-based pedestrian collision warning system with crosswalk detection",
         authors="Suzuki, Raksincharoensak, Shimizu, Nagai, Adomat", group="算法系统"),
    dict(key="sun2023rl", doi="10.1061/9780784484869.024", year=2023,
         title="A Reinforcement Learning-Based Adaptive Forward Collision Warning System by Considering Drivers' Reaction Time in Real Time",
         authors="Sun, Wu, Gong, Yang", group="算法系统"),
    dict(key="kuo2016pcw", doi="10.1109/is3c.2016.189", year=2016,
         title="Pedestrian Collision Warning of Advanced Driver Assistance Systems",
         authors="Kuo, Fu, Tsai, Lin, Chang", group="算法系统"),
    dict(key="zhangy2023path", doi="10.1109/ictis60134.2023.10243767", year=2023,
         title="Research on Pedestrian Vehicle Collision Warning Based on Path Prediction",
         authors="Zhang, Wang, Zhuo, Jiao, Yang", group="算法系统"),
    dict(key="kim2020p2cws", doi="", year=2020, arxiv="2009.10868",
         title="A Real-Time Predictive Pedestrian Collision Warning Service for Cooperative Intelligent Transportation Systems Using 3D Pose Estimation",
         authors="Kim, Ka, Yeo, Kim", group="算法系统"),
    dict(key="joo2024rate", doi="10.2139/ssrn.4927850", year=2024,
         title="Predictive Safety-Aware Transmit Rate Control Scheme for Real-Time Proactive Forward Collision Warning System",
         authors="Joo, Kim, Kim", group="算法系统"),
    dict(key="miyoshi2005sae", doi="10.4271/2005-08-0554", year=2005,
         title="Development of Forward-Collision Avoidance Warning System Adapted for Driver Characteristics",
         authors="Miyoshi, Nagai, Kamada, Yoshida", group="算法系统"),
    dict(key="elliott2019cav", doi="10.1016/j.jtte.2018.09.005", year=2019,
         title="Recent advances in connected and automated vehicles",
         authors="Elliott, Keen, Miao", group="综述人因"),
    dict(key="rasouli2019survey", doi="10.1109/tits.2019.2901817", year=2019, arxiv="1805.11773",
         title="Autonomous Vehicles That Interact With Pedestrians: A Survey of Theory and Practice",
         authors="Rasouli, Tsotsos", group="综述人因"),
    dict(key="amini2019negotiation", doi="10.3390/su11236713", year=2019,
         title="Negotiation and Decision-Making for a Pedestrian Roadway Crossing: A Literature Review",
         authors="Amini, Katrakazas, Antoniou", group="综述人因"),
    dict(key="takada_decel", doi="", year=2010,
         title="Effectiveness of forward obstacles collision warning system based on deceleration for collision avoidance",
         authors="Takada, Hiraoka, Kawakami", group="综述人因"),
    dict(key="gray2014vibro", doi="10.1371/journal.pone.0087070", year=2014,
         title="A Comparison of Different Informative Vibrotactile Forward Collision Warnings: Does the Warning Need to Be Linked to the Collision Event?",
         authors="Gray, Ho, Spence", group="综述人因"),
    dict(key="saej2400", doi="10.4271/j2400_200308", year=2003,
         title="Human Factors in Forward Collision Warning Systems: Operating Characteristics and User Interface Requirements",
         authors="SAE ADAS Committee", group="综述人因"),
    dict(key="coelingh2010cwab", doi="10.1109/itsc.2010.5625077", year=2010,
         title="Collision Warning with Full Auto Brake and Pedestrian Detection - a practical example of Automatic Emergency Braking",
         authors="Coelingh, Eidehall, Bengtsson", group="综述人因"),
]

SKIP_KEYS = {"lubbe2017", "kim2018tvcg", "kim2016shadow", "ye2025plane2",
             "jung2016cnn", "banerjee2021pcw", "kim2020p2cws"}

if __name__ == "__main__":
    import json
    import pathlib
    import re
    root = pathlib.Path("/home/gezhuocheng/HUD")
    meta = json.load(open(root / "papers_metadata.json"))

    def n(t):
        return re.sub(r"[^a-z0-9]", "", (t or "").lower())[:45]

    have_doi = {p.get("doi", "").lower() for p in meta if p.get("doi")}
    have_title = {n(p.get("title")): p for p in meta}
    log1 = json.load(open(root / "scripts" / "new_download_log.json"))
    have_doi |= {v["doi"].lower() for v in log1.values() if v.get("doi")}

    new, exist = [], []
    for r in REFS2:
        hit = (r["doi"] and r["doi"].lower() in have_doi) or have_title.get(n(r["title"]))
        (exist if hit else new).append(r)
    print(f"list2 total {len(REFS2)}  already {len(exist)}  NEW {len(new)}")
    for r in exist:
        print("  HAVE", r["key"], r["title"][:60])
    print()
    for i, r in enumerate(new, 1):
        print(f"  {i:2d}. {r['key']:20s} {r['doi'] or ('arXiv:' + r.get('arxiv', '-')):40s} {r['title'][:60]}")
