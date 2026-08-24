#!/usr/bin/env python3
"""Structured entries parsed from ar-hud参考文献列表.md, deduped by DOI."""

REFS = [
    dict(key="ieee10154473", doi="10.1109/access.2023.3286872", year=2023,
         title="Augmented Reality-Based Navigation Using Deep Learning-Based Pedestrian and Personal Mobility User Recognition—A Comparative Evaluation for Driving Assistance",
         url="https://ieeexplore.ieee.org/document/10154473", authors="Roh et al."),
    dict(key="bolton2015", doi="10.1145/2799250.2799253", year=2015,
         title="An investigation of augmented reality presentations of landmark-based navigation using a head-up display",
         url="", authors="Bolton, Burnett, Large"),
    dict(key="chenh2026", doi="10.1111/nyas.70167", year=2026,
         title="Hierarchical feature evaluation and decision-making for in-vehicle augmented-reality head-up display based on Pythagorean Hamacher aggregation",
         url="", authors="Chen H. et al."),
    dict(key="chenw2025ca", doi="10.1080/10447318.2024.2327197", year=2025,
         title="Evaluating the effectiveness of contact-analog and bounding box prototypes in augmented reality head-up display warning for Chinese novice drivers",
         url="", authors="Chen W. et al."),
    dict(key="chenw2025pri", doi="10.1080/10447318.2024.2439572", year=2025,
         title="Priority Design in Multi-Target AR-HUD Warning: Evidence from Eye Movement and Behavior of the Novice Driver",
         url="", authors="Chen W. et al."),
    dict(key="chenw2023ib", doi="10.1080/15389588.2023.2186735", year=2023,
         title="Inattentional blindness to unexpected hazard in augmented reality head-up display assisted driving: The impact of the relative position between stimulus and augmented graph",
         url="", authors="Chen W. et al."),
    dict(key="chenw2019ped", doi="10.1016/j.trf.2019.07.004", year=2019,
         title="Drivers' recognition of pedestrian road-crossing intentions: Performance and process",
         url="", authors="Chen, Zhuang, Cui, Ma"),
    dict(key="cheng2023trip", doi="10.1016/j.trip.2023.100767", year=2023,
         title="Does the AR-HUD system affect driving behaviour? An eye-tracking experiment study",
         url="", authors="Cheng, Zhong, Tian"),
    dict(key="wintersberger2018", doi="10.1162/pres_a_00320", year=2018,
         title="Fostering User Acceptance and Trust in Fully Automated Vehicles: Evaluating the Potential of Augmented Reality",
         url="https://direct.mit.edu/pvar/article-abstract/27/1/46/96082", authors="Wintersberger et al."),
    dict(key="graphsim2021", doi="10.1109/ITSC48978.2021.9561107", year=2021,
         title="Graph-SIM: A Graph-based Spatiotemporal Interaction Modelling for Pedestrian Action Prediction",
         url="https://ieeexplore.ieee.org/document/9561107", authors="Zhang et al."),
    dict(key="hou2025dyn", doi="10.1080/10447318.2024.2400376", year=2025,
         title="The Effect of Dynamic Effects and Color Transparency of AR-HUD Navigation Graphics on Driving Behavior Regarding Inattentional Blindness",
         url="", authors="Hou, Dong, Wang"),
    dict(key="jing2022", doi="10.1080/15389588.2022.2055752", year=2022,
         title="The impact of different AR-HUD virtual warning interfaces on the takeover performance and visual characteristics of autonomous vehicles",
         url="", authors="Jing et al."),
    dict(key="karatas2020", doi="10.1109/IV47402.2020.9304610", year=2020,
         title="Evaluation of AR-HUD interface during an automated intervention in manual driving",
         url="", authors="Karatas et al."),
    dict(key="kettle2022", doi="10.3390/safety8040084", year=2022,
         title="Augmented Reality for Vehicle-Driver Communication: A Systematic Review",
         url="", authors="Kettle, Lee"),
    dict(key="kim2022dist", doi="10.1177/0018720819844845", year=2022,
         title="Assessing Distraction Potential of Augmented Reality Head-Up Displays for Vehicle Drivers",
         url="", authors="Kim, Gabbard"),
    dict(key="langlois2016", doi="10.1109/ITSC.2016.7795767", year=2016,
         title="Augmented reality versus classical HUD to take over from automated driving: An aid to smooth reactions and to anticipate maneuvers",
         url="", authors="Langlois, Soualmi"),
    dict(key="lij2025fog", doi="10.3390/app152011072", year=2025,
         title="The Influence of Information Redundancy on Driving Behavior and Psychological Responses under Different Fog and Risk Conditions",
         url="", authors="Li, Chen, Chen"),
    dict(key="lij2025opa", doi="10.1002/jsid.2096", year=2025,
         title="Effects of driving background complexity and interface opacity on visual cognition in AR-HUD systems",
         url="", authors="Li, Wang, Chen"),
    dict(key="lopez2025", doi="10.1016/j.apergo.2025.104610", year=2025,
         title="Opacity in car augmented reality head-up displays: Users' preferences, visual attention, and situation awareness",
         url="", authors="Lopez, Moacdieh"),
    dict(key="ma2024eid", doi="10.3390/s24248010", year=2024,
         title="Design and Evaluation of Ecological Interface of Driving Warning System Based on AR-HUD",
         url="", authors="Ma, Li, Zuo"),
    dict(key="merenda2018", doi="10.1109/TVCG.2018.2868531", year=2018,
         title="Augmented Reality Interface Design Approaches for Goal-directed and Stimulus-driven Driving Tasks",
         url="", authors="Merenda et al."),
    dict(key="pammer2013", doi="10.1016/j.aap.2012.07.026", year=2013,
         title="Attentional differences in driving judgments for country and city scenes: Semantic congruency in inattentional blindness",
         url="", authors="Pammer, Blink"),
    dict(key="park2013eff", doi="10.1007/978-3-642-39238-2_43", year=2013,
         title="Efficient Information Representation Method for Driver-Centered AR-HUD System",
         url="", authors="Park, Kim"),
    dict(key="pfann2015", doi="10.1016/j.promfg.2015.07.678", year=2015,
         title="A Comparison of Display Concepts for a Navigation System in an Automotive Contact Analog Head-up Display",
         url="", authors="Pfannmüller et al."),
    dict(key="strayer2025", doi="10.1146/annurev-vision-110423-025626", year=2025,
         title="SPIDER 2.0: Driver Distraction and Visual Attention",
         url="", authors="Strayer, McDonnell"),
    dict(key="wangj2024dyn", doi="10.1016/j.ijhcs.2023.103194", year=2024,
         title="A new dynamic spatial information design framework for AR-HUD to evoke drivers' instinctive responses and improve accident prevention",
         url="", authors="Wang J. et al."),
    dict(key="wangy2021ib", doi="10.1080/10447318.2021.1970434", year=2021,
         title="Inattentional Blindness in Augmented Reality Head-Up Display-Assisted Driving",
         url="", authors="Wang Y. et al."),
    dict(key="wei2025inter", doi="10.1109/CVCI66304.2025.11348153", year=2025,
         title="Study on AR-HUD design in unprotected intersection scenario under autonomous driving",
         url="", authors="Wei C. et al."),
    dict(key="winklerm2025rev", doi="10.1080/10447318.2024.2443252", year=2025,
         title="A Review of Augmented Reality Heads Up Display in Vehicles: Effectiveness, Application, and Safety",
         url="", authors="Winkler M., Soleimani"),
    dict(key="winklers2018", doi="10.1016/j.aap.2018.01.040", year=2018,
         title="How to warn drivers in various safety-critical situations – Different strategies, different reactions",
         url="", authors="Winkler S., Kazazi, Vollrath"),
    dict(key="wuz2024icon", doi="10.3390/su16219167", year=2024,
         title="Comparative Analysis of AR-HUDs Crash Warning Icon Designs: An Eye-Tracking Study Using 360° Panoramic Driving Simulation",
         url="", authors="Wu Z. et al."),
    dict(key="wuz2024take", doi="10.1080/10447318.2023.2254645", year=2024,
         title="The Effect of AR-HUD Takeover Assistance Types on Driver Situation Awareness in Highly Automated Driving: A 360-Degree Panorama Experiment",
         url="", authors="Wu Z. et al."),
    dict(key="yamin2024guide", doi="10.1016/j.trf.2024.06.001", year=2024,
         title="In-vehicle human–machine interface guidelines for augmented reality head-up displays: A review, guideline formulation, and future research directions",
         url="", authors="Yamin, Park, Kim"),
    dict(key="ye2025plane", doi="10.3390/electronics14234768", year=2025,
         title="Spatial Plane Positioning of AR-HUD Graphics: Implications for Driver Inattentional Blindness in Navigation and Collision Warning Scenarios",
         url="", authors="Ye, Yin"),
    dict(key="you2024coop", doi="10.1080/10447318.2023.2233734", year=2024,
         title="A Novel Cooperation-Guided Warning of Invisible Danger from AR-HUD to Enhance Driver's Perception",
         url="", authors="You F. et al."),
    dict(key="yuk2024emoji", doi="10.1080/15389588.2024.2337120", year=2024,
         title="Effects of a color gradient and emoji in AR-HUD warning interfaces in autonomous vehicles on takeover performance and driver emotions",
         url="", authors="Yu K. et al."),
    dict(key="yunuo2023ijvd", doi="10.1504/IJVD.2023.133262", year=2023,
         title="How does AR-HUD system affect driving behaviour? Evidence from an eye-tracking experiment study",
         url="", authors="Yunuo, Xia, Liwei"),
    dict(key="zeng2024fog", doi="10.1117/12.3054840", year=2024,
         title="The impact of AR-HUD lane enhancement on lateral control performance under fog conditions",
         url="", authors="Zeng M. et al."),
    dict(key="zhu2025sal", doi="10.1109/ACCESS.2025.3588576", year=2025,
         title="Visual Saliency Design for AR-HUD Navigation in Extreme Weather: Reducing Inattentional Blindness",
         url="", authors="Zhu, Li, Liu"),
]

if __name__ == "__main__":
    import json
    import pathlib
    root = pathlib.Path("/home/gezhuocheng/HUD")
    meta = json.load(open(root / "papers_metadata.json"))
    have = {}
    for p in meta:
        have[p.get("doi", "").lower()] = p

    def norm_title(t):
        import re
        return re.sub(r"[^a-z0-9]", "", t.lower())[:60]

    have_titles = {norm_title(p["title"]): p for p in meta}

    new, exist = [], []
    for r in REFS:
        d = r["doi"].lower()
        hit = have.get(d) or have_titles.get(norm_title(r["title"]))
        if hit:
            exist.append((r["key"], hit["idx"], hit["title"][:60]))
        else:
            new.append(r)

    print(f"total unique refs: {len(REFS)}  already have: {len(exist)}  NEW: {len(new)}")
    print("\n--- already in papers/ ---")
    for k, idx, t in exist:
        print(f"  {k:16s} -> #{idx:02d} {t}")
    print("\n--- NEW to download ---")
    for i, r in enumerate(new, 1):
        print(f"  {i:2d}. {r['key']:16s} {r['doi']:42s} {r['title'][:70]}")
