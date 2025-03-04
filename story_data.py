
# This file contains all the story content for the Cosmic Odyssey game
# It defines a dictionary (STORY_DATA) where:
# - Each key is a scene identifier (string)
# - Each value is a dictionary containing the scene's description and choices
# - Each choice has display text and the next scene it leads to

STORY_DATA = {
    # Starting scene of the game - player is introduced to the mission
    "start": {
        "description": "You are Commander of an lunar mission. Your spacecraft has just landed on the far side of the moon. Your mission: explore an unusual signal detected by Earth's observatories. Through the viewport, you see the desolate lunar landscape stretching to the horizon.",
        "choices": [
            {
                "text": "Check mission briefing on the ship's computer",
                "next_scene": "computer_check"
            },
            {
                "text": "Look closer at the lunar surface",
                "next_scene": "examine_surface"
            },
            {
                "text": "Try to contact mission control",
                "next_scene": "contact_control"
            }
        ]
    },
    
    # Scene for checking the mission briefing
    "computer_check": {
        "description": "The mission briefing shows that the signal originates from a region called the dark side. Scientists believe it might be evidence of subsurface water or possibly something more unusual. Your job is to investigate and collect samples.",
        "choices": [
            {
                "text": "Run a diagnostic on your equipment",
                "next_scene": "run_diagnostic"
            },
            {
                "text": "Search the database for more information",
                "next_scene": "search_database"
            }
        ]
    },
    
    # Scene for equipment diagnostic
    "run_diagnostic": {
        "description": "The diagnostic confirms your lunar rover, life support, and scientific equipment are all functioning normally. The surface temperature is -173°C in the shadows and 127°C in direct sunlight. Your suit can handle both extremes.",
        "choices": [
            {
                "text": "Prepare the rover for exploration",
                "next_scene": "prepare_rover"
            },
            {
                "text": "Check oxygen and water reserves",
                "next_scene": "check_supplies"
            }
        ]
    },
    
    # Scene for checking supplies
    "check_supplies": {
        "description": "Your supplies are adequate for a 72-hour expedition. The recycling systems are functioning at optimal capacity, converting CO2 back to breathable oxygen. Water reserves are at 98%.",
        "choices": [
            {
                "text": "Begin preparations for surface walk",
                "next_scene": "suit_up"
            },
            {
                "text": "Double-check the rover systems",
                "next_scene": "prepare_rover"
            }
        ]
    },
    
    # Scene for preparing the rover
    "prepare_rover": {
        "description": "The lunar rover is operational and ready for deployment. Its solar panels are fully charged, giving you a range of about 200 kilometers before needing to recharge. The navigation system is calibrated to the lunar surface.",
        "choices": [
            {
                "text": "Deploy the rover and begin exploration",
                "next_scene": "deploy_rover"
            },
            {
                "text": "Equip yourself for a preliminary walk",
                "next_scene": "suit_up"
            }
        ]
    },
    
    # Scene for suiting up
    "suit_up": {
        "description": "You put on your EVA suit, conducting a meticulous check of all seals and systems. The heads-up display shows green across the board. You're ready to step onto the lunar surface.",
        "choices": [
            {
                "text": "Exit the airlock",
                "next_scene": "first_steps"
            },
            {
                "text": "Wait for optimal solar conditions",
                "next_scene": "wait_conditions"
            }
        ]
    },
    
    # Scene for waiting for optimal conditions
    "wait_conditions": {
        "description": "After waiting for the sun to be at the right angle, reducing extreme temperature variations, you're ready to proceed with your exploration in more favorable conditions.",
        "choices": [
            {
                "text": "Exit the airlock",
                "next_scene": "first_steps"
            },
            {
                "text": "Use the time to check the signal location",
                "next_scene": "check_signal"
            }
        ]
    },
    
    # Scene for searching the database
    "search_database": {
        "description": "The database reveals that similar signals have been detected before but never investigated. Theoretical explanations range from natural geological processes to the tantalizing possibility of ice caverns or ancient hollow lava tubes.",
        "choices": [
            {
                "text": "Focus on geological possibilities",
                "next_scene": "geology_research"
            },
            {
                "text": "Investigate the lava tube theories",
                "next_scene": "lava_tubes"
            }
        ]
    },
    
    # Scene for examining the lunar surface
    "examine_surface": {
        "description": "The lunar surface is covered in regolith - fine dust that's been pulverized by billions of years of meteorite impacts. In the distance, you notice an unusual formation that doesn't match the surrounding terrain.",
        "choices": [
            {
                "text": "Take photos of the formation",
                "next_scene": "take_photos"
            },
            {
                "text": "Prepare for a closer look",
                "next_scene": "suit_up"
            }
        ]
    },
    
    # Scene for taking photos
    "take_photos": {
        "description": "You capture high-resolution images of the unusual formation. The computer analysis suggests it might be the entrance to a lava tube - a natural underground tunnel formed by ancient lunar volcanic activity.",
        "choices": [
            {
                "text": "Send the photos to mission control",
                "next_scene": "send_photos"
            },
            {
                "text": "Prepare for surface exploration",
                "next_scene": "suit_up"
            }
        ]
    },
    
    # Scene for contacting mission control
    "contact_control": {
        "description": "You establish communication with mission control on Earth. There's a 2.6-second delay due to distance. They confirm your mission parameters and stress the importance of investigating the signal while maintaining safety protocols.",
        "choices": [
            {
                "text": "Ask for additional information about the signal",
                "next_scene": "signal_info"
            },
            {
                "text": "Report your readiness to begin exploration",
                "next_scene": "report_ready"
            }
        ]
    },
    
    # Scene for signal information
    "signal_info": {
        "description": "Mission control provides additional details: the signal appears to be rhythmic and has characteristics that suggest it might be related to subsurface water movement or thermal expansion/contraction cycles in the lunar regolith.",
        "choices": [
            {
                "text": "Prepare specialized equipment for analysis",
                "next_scene": "special_equipment"
            },
            {
                "text": "Begin surface exploration",
                "next_scene": "suit_up"
            }
        ]
    },
    
    # Scene for first steps on the moon
    "first_steps": {
        "description": "You take your first steps on the lunar surface. The sensation is surreal - you weigh only one-sixth of your Earth weight. The desolate beauty of the landscape is breathtaking, with stars visible even during the lunar day.",
        "choices": [
            {
                "text": "Collect surface samples",
                "next_scene": "collect_samples"
            },
            {
                "text": "Head toward the signal source",
                "next_scene": "move_to_signal"
            }
        ]
    },
    
    # Scene for collecting samples
    "collect_samples": {
        "description": "You collect various lunar regolith samples, carefully storing them in labeled containers. One sample has unusual properties - it contains crystals that weren't expected in this region of the moon.",
        "choices": [
            {
                "text": "Analyze the crystals on-site",
                "next_scene": "analyze_crystals"
            },
            {
                "text": "Continue toward the signal source",
                "next_scene": "move_to_signal"
            }
        ]
    },
    
    # Scene for analyzing crystals
    "analyze_crystals": {
        "description": "Your portable analyzer indicates the crystals contain traces of water molecules! This is a significant discovery that suggests this region might have more subsurface water than previously thought.",
        "choices": [
            {
                "text": "Report findings to mission control",
                "next_scene": "report_discovery"
            },
            {
                "text": "Continue exploration toward the signal",
                "next_scene": "move_to_signal"
            }
        ]
    },
    
    # Scene for moving to the signal source
    "move_to_signal": {
        "description": "You travel across the lunar surface toward the signal source. As you get closer, you discover what appears to be the entrance to a vast cavern - potentially a lava tube that could be large enough to house a future lunar base.",
        "choices": [
            {
                "text": "Set up monitoring equipment outside",
                "next_scene": "setup_equipment"
            },
            {
                "text": "Cautiously enter the cavern",
                "next_scene": "enter_cavern"
            }
        ]
    },
    
    # Scene for setting up equipment
    "setup_equipment": {
        "description": "You set up seismic, thermal, and radiation monitoring equipment near the cavern entrance. Initial readings show stable conditions and confirm that the signal is definitely coming from inside the cavern.",
        "choices": [
            {
                "text": "Prepare to enter the cavern",
                "next_scene": "enter_cavern"
            },
            {
                "text": "Send a drone in first",
                "next_scene": "send_drone"
            }
        ]
    },
    
    # Scene for sending a drone
    "send_drone": {
        "description": "The drone sends back fascinating footage. The cavern extends deep into the lunar crust and contains what appears to be ice formations. The drone also detects unusual electromagnetic readings deeper inside.",
        "choices": [
            {
                "text": "Enter the cavern to investigate",
                "next_scene": "enter_cavern"
            },
            {
                "text": "Report findings and await instructions",
                "next_scene": "report_discovery"
            }
        ]
    },
    
    # Scene for entering the cavern
    "enter_cavern": {
        "description": "You enter the lunar cavern, your headlamp illuminating a vast space untouched by humanity. The temperature is surprisingly stable, and your instruments detect trace amounts of water vapor in the air. The cave extends farther than your light can reach.",
        "choices": [
            {
                "text": "Collect samples from the cave walls",
                "next_scene": "cave_samples"
            },
            {
                "text": "Proceed deeper following the signal",
                "next_scene": "deeper_exploration"
            }
        ]
    },
    
    # Scene for collecting cave samples
    "cave_samples": {
        "description": "The samples from the cave walls contain significant amounts of ice! This could be a crucial water source for future lunar colonies. As you examine the ice, you notice it has a slightly unusual molecular structure.",
        "choices": [
            {
                "text": "Analyze the unusual structure",
                "next_scene": "analyze_ice"
            },
            {
                "text": "Continue deeper into the cavern",
                "next_scene": "deeper_exploration"
            }
        ]
    },
    
    # Scene for deeper exploration
    "deeper_exploration": {
        "description": "As you venture deeper, the cavern opens into an enormous chamber. In the center, you discover the source of the signal: a natural formation of lunar crystals that expand and contract with temperature changes, creating resonant frequencies that Earth's instruments detected as a signal.",
        "choices": [
            {
                "text": "Study the crystal formation",
                "next_scene": "study_crystals"
            },
            {
                "text": "Explore the rest of the chamber",
                "next_scene": "explore_chamber"
            }
        ]
    },
    
    # Scene for studying crystals
    "study_crystals": {
        "description": "The crystal formation appears to be sensitive to thermal and gravitational changes, effectively making it a natural scientific instrument that has been recording lunar conditions for potentially millions of years. This is an extraordinary scientific discovery!",
        "choices": [
            {
                "text": "Collect crystal samples",
                "next_scene": "final_discovery"
            },
            {
                "text": "Set up permanent monitoring equipment",
                "next_scene": "final_discovery"
            }
        ]
    },
    
    # Scene for exploring the chamber
    "explore_chamber": {
        "description": "Further exploration of the chamber reveals a network of smaller caverns, all containing various forms of the same crystal formations. You've discovered not just a potential site for a lunar base, but a natural laboratory of incalculable scientific value.",
        "choices": [
            {
                "text": "Map the entire cavern system",
                "next_scene": "final_discovery"
            },
            {
                "text": "Begin comprehensive sample collection",
                "next_scene": "final_discovery"
            }
        ]
    },
    
    # Scene for final discovery - one of the ending scenes
    "final_discovery": {
        "description": "Your exploration of the lunar caverns has yielded discoveries beyond all expectations: a stable environment with access to water ice, natural protection from radiation, and crystal formations that could revolutionize our understanding of lunar geology. Your mission is a historic success that will shape the future of lunar exploration and potential colonization.",
        "choices": []  # No choices indicates this is an ending
    },
    
    # Scene for reporting discovery - another ending scene
    "report_discovery": {
        "description": "Mission control is ecstatic about your discoveries. They inform you that your findings have already led to funding approval for a permanent lunar research station at this location. Your name will go down in history alongside the greatest explorers of all time.",
        "choices": []  # No choices indicates this is an ending
    },
    
    # Scene for reporting readiness
    "report_ready": {
        "description": "You report your readiness to begin the mission. Mission control gives you the green light, reminding you that you're making history with every step on this unexplored region of the moon.",
        "choices": [
            {"text": "Begin preparations for surface walk", "next_scene": "suit_up"},
            {"text": "Double-check mission objectives", "next_scene": "computer_check"}
        ]
    },
    
    # Scene for deploying the rover
    "deploy_rover": {
        "description": "You deploy the lunar rover and begin your journey across the cratered landscape. The rover handles the terrain well, climbing over small craters and navigating around larger obstacles.",
        "choices": [
            {"text": "Head directly to the signal source", "next_scene": "move_to_signal"},
            {"text": "Take a survey of the surrounding area first", "next_scene": "survey_area"}
        ]
    },
    
    # Scene for surveying the area
    "survey_area": {
        "description": "Your survey reveals several interesting geological features. You notice what appears to be a relatively recent impact crater with unusual ejecta patterns and another area where the regolith seems to have been disturbed in a non-impact pattern.",
        "choices": [
            {"text": "Investigate the unusual crater", "next_scene": "investigate_crater"},
            {"text": "Check out the disturbed regolith", "next_scene": "check_disturbance"}
        ]
    },
    
    # Scene for checking the signal
    "check_signal": {
        "description": "The signal appears to be coming from about 5 kilometers east of your landing site. It sits in the shadow of a large crater rim, which might explain why it wasn't detected by earlier missions.",
        "choices": [
            {"text": "Begin your surface walk", "next_scene": "first_steps"},
            {"text": "Prepare the rover for a longer journey", "next_scene": "prepare_rover"}
        ]
    },
    
    # Scene for geological research
    "geology_research": {
        "description": "The geological data suggests that this region might contain skylights - collapsed sections of lava tube ceilings that provide natural access to underground caverns. These could be ideal locations for future lunar habitats.",
        "choices": [
            {"text": "Look for skylights during your exploration", "next_scene": "suit_up"},
            {"text": "Research the potential habitability of lava tubes", "next_scene": "lava_tubes"}
        ]
    },
    
    # Scene for investigating lava tubes
    "lava_tubes": {
        "description": "Lunar lava tubes are potentially enormous compared to those on Earth due to the moon's lower gravity. Research suggests they could be stable environments protected from radiation, micrometeorites, and extreme temperature fluctuations - perfect for human habitation.",
        "choices": [
            {"text": "Begin exploration focusing on finding lava tubes", "next_scene": "suit_up"},
            {"text": "Check if the signal could be coming from a lava tube", "next_scene": "check_signal"}
        ]
    },
    
    # Scene for sending photos
    "send_photos": {
        "description": "Mission control confirms your analysis - the formation appears to be a skylight into a lava tube. They're excited about the potential significance and urge you to investigate carefully while following all safety protocols.",
        "choices": [
            {"text": "Prepare for surface exploration", "next_scene": "suit_up"},
            {"text": "Request additional analysis from Earth", "next_scene": "wait_analysis"}
        ]
    },
    
    # Scene for special equipment
    "special_equipment": {
        "description": "You prepare specialized equipment for signal analysis, including ground-penetrating radar and sensitive seismographs. These tools should help you pinpoint the exact source and nature of the mysterious signal.",
        "choices": [
            {"text": "Begin surface exploration with equipment", "next_scene": "suit_up"},
            {"text": "Conduct preliminary scans from the lander", "next_scene": "prelim_scans"}
        ]
    },
    
    # Scene for analyzing ice
    "analyze_ice": {
        "description": "The ice analysis reveals something extraordinary - the water contains isotope ratios different from Earth's water. This suggests it might have a different origin, potentially providing new insights into the moon's formation and history.",
        "choices": [
            {"text": "Report this major finding", "next_scene": "report_discovery"},
            {"text": "Continue your exploration", "next_scene": "deeper_exploration"}
        ]
    },
    
    # Scene for investigating crater
    "investigate_crater": {
        "description": "The crater investigation reveals unusual mineral compositions in the impact ejecta, suggesting this meteorite may have originated from a different part of the solar system than most lunar impactors. You collect valuable samples for return to Earth.",
        "choices": [
            {"text": "Head to the signal source now", "next_scene": "move_to_signal"},
            {"text": "Check the other unusual area first", "next_scene": "check_disturbance"}
        ]
    },
    
    # Scene for checking disturbance
    "check_disturbance": {
        "description": "The disturbed area appears to be a partial collapse revealing a small opening into a subsurface void. Your sensors indicate it connects to a larger underground system - possibly related to the main signal source.",
        "choices": [
            {"text": "Investigate this secondary entrance", "next_scene": "secondary_entrance"},
            {"text": "Proceed to the main signal source", "next_scene": "move_to_signal"}
        ]
    },
    
    # Scene for secondary entrance
    "secondary_entrance": {
        "description": "This secondary entrance leads to the same cavern system as the main signal source, but from a different angle. You've discovered a potential emergency exit/entrance for future missions - an important safety feature for any permanent lunar base.",
        "choices": [
            {"text": "Connect with the main exploration route", "next_scene": "deeper_exploration"},
            {"text": "Map this secondary tunnel system", "next_scene": "map_tunnels"}
        ]
    },
    
    # Scene for mapping tunnels
    "map_tunnels": {
        "description": "Your mapping reveals an extensive network of interconnected lava tubes spanning several kilometers. This could support a substantial lunar colony with different areas for habitation, research, agriculture, and manufacturing, all protected from the harsh surface conditions.",
        "choices": [
            {"text": "Complete your exploration of the main cavern", "next_scene": "deeper_exploration"},
            {"text": "Return to report this remarkable discovery", "next_scene": "report_discovery"}
        ]
    },
    
    # Scene for waiting for analysis
    "wait_analysis": {
        "description": "Additional analysis confirms your findings and provides more details about the potential subterranean structure. Mission control gives you the go-ahead to proceed with direct exploration.",
        "choices": [
            {"text": "Begin your surface walk", "next_scene": "first_steps"},
            {"text": "Prepare the rover for exploration", "next_scene": "prepare_rover"}
        ]
    },
    
    # Scene for preliminary scans
    "prelim_scans": {
        "description": "Preliminary scans narrow down the signal's location and characteristics. It appears to be coming from about 20 meters below the surface, in what might be a hollow area consistent with a lava tube or similar formation.",
        "choices": [
            {"text": "Begin surface exploration", "next_scene": "suit_up"},
            {"text": "Conduct more detailed remote sensing", "next_scene": "detailed_sensing"}
        ]
    },
    
    # Scene for detailed sensing
    "detailed_sensing": {
        "description": "Your detailed sensing creates a 3D map of the subsurface structure. It confirms a large lava tube with several chambers, one of which contains the source of the signal. The data will be invaluable for safe exploration.",
        "choices": [
            {"text": "Begin surface exploration with this map", "next_scene": "suit_up"},
            {"text": "Share the detailed map with mission control", "next_scene": "share_map"}
        ]
    },
    
    # Scene for sharing map
    "share_map": {
        "description": "Mission control is impressed with your thoroughness. They provide additional guidance based on your map and recommend the safest approach route. They also note that this level of detail will be essential for planning any future lunar base at this location.",
        "choices": [
            {"text": "Begin exploration following their guidance", "next_scene": "suit_up"},
            {"text": "Make final preparations before heading out", "next_scene": "final_prep"}
        ]
    },
    
    # Scene for final preparations
    "final_prep": {
        "description": "With all preparations complete, you've done everything possible to ensure a safe and productive exploration. Your equipment is ready, your path is planned, and you're about to make history.",
        "choices": [
            {"text": "Begin your historic lunar exploration", "next_scene": "first_steps"}
        ]
    },
    
    # Generic game over scene
    "game_over": {
        "description": "Your lunar exploration has come to an end. The decisions you made have led you here, forever changing our understanding of Earth's closest celestial neighbor.",
        "choices": []  # No choices indicates this is an ending
    }
}
