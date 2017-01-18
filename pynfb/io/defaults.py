from collections import OrderedDict

general_defaults = OrderedDict([
    #('bDoubleBlind', False),
    #('bShowFBCount', False),
    #('bShowFBRect', False),
    #('fSamplingFrequency', ''),
    #('CompositeMontage', '__'),
    #('CSPSettings', OrderedDict([
    #    ('iNComp', '2'),
    #    ('dInitBand', '8 16')]))
])


vectors_defaults = OrderedDict([
    ('bDC', 0),
    ('sExperimentName', 'experiment'),
    ('sInletType', 'lsl'),
    ('sStreamName', 'NVX136_Data'),
    ('sRawDataFilePath', ''),
    ('sFTHostnamePort', 'localhost:1972'),
    ('bPlotRaw', 1),
    ('bPlotSignals', 1),
    ('fRewardPeriodS', 0.25),
    ('sReference', ''),
    ('sReferenceSub', ''),
    ('vSignals', OrderedDict([
        ('DerivedSignal', [OrderedDict([     # DerivedSignal is list!
            ('sSignalName', 'Signal'),
            ('SpatialFilterMatrix', ''),
            ('bDisableSpectrumEvaluation', 0),
            ('fSmoothingFactor', 0.3),
            ('fFFTWindowSize', 500),
            ('fBandpassLowHz', 0),
            ('fBandpassHighHz', 250),
            ('fAverage', ''),
            ('fStdDev', ''),
            # ('sType', 'plain')
        ])]),
        ('CompositeSignal', [OrderedDict([     # DerivedSignal is list!
            ('sSignalName', 'Composite'),
            ('sExpression', '')
        ])])
    ])),
    ('vProtocols', OrderedDict([
        ('FeedbackProtocol', [OrderedDict([  # FeedbackProtocol is list!
            ('sProtocolName', 'Protocol'),
            # ('sSignalComposition', 'Simple'),
            # ('nMSecondsPerWindow', ''),
            ('bUpdateStatistics', 0),
            ('iDropOutliers', 0),
            ('bSSDInTheEnd', 0),
            # ('bStopAfter', False),
            # ('bShowFBRect', False),
            ('fDuration', 10),
            # ('fThreshold', ''),
            ('fbSource', 'All'),
            # ('iNComp', ''),
            ('sFb_type', 'Baseline'),
            # ('dBand', ''),
            ('cString', ''),
            ('bUseExtraMessage', 0),
            ('cString2', ''),
            ('fBlinkDurationMs', 50),
            ('fBlinkThreshold', 0),
            ('sMockSignalFilePath', ''),
            ('sMockSignalFileDataset', 'protocol1'),
            ('iMockPrevious', 0),
            ('bReverseMockPrevious', 0),
            ('sRewardSignal', ''),
            ('bRewardThreshold', 0),
            ('bShowReward', 0),
            ('bPauseAfter', 0),
            ('iRandomBound', 0),
            ('sVideoPath', ''),
            ('sMSignal', 'None'),
            ('fMSignalThreshold', 1)
        ])])])),
    ('vPSequence', OrderedDict([
        ('s', ['Protocol'])])),
])