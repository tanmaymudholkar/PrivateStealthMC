# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: Configuration/GenProduction/python/SUS-RunIIFall17FSPremix-00069-fragment.py --fileout file:SUS-RunIIFall17FSPremix-00069.root --pileup_input /store/mc/RunIIFall17FSPrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUMoriond17_94X_mc2017_realistic_v15-v1/20005/5610116F-3EFA-E811-BACE-FA163EC04576.root --mc --eventcontent AODSIM --fast --datatier AODSIM --conditions 94X_mc2017_realistic_v15 --beamspot Realistic25ns13TeVEarly2017Collision --customise_commands process.source.numberEventsInLuminosityBlock = cms.untracked.uint32(200) --step GEN,SIM,RECOBEFMIX,DIGIPREMIX_S2,DATAMIX,L1,DIGI2RAW,L1Reco,RECO --datamix PreMix --era Run2_2017_FastSim --python_filename SUS-RunIIFall17FSPremix-00069_1_cfg.py --no_exec
import FWCore.ParameterSet.Config as cms

from Configuration.StandardSequences.Eras import eras

process = cms.Process('RECO',eras.Run2_2017_FastSim,eras.fastSim)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('FastSimulation.Configuration.Geometries_MC_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('Configuration.StandardSequences.Generator_cff')
process.load('IOMC.EventVertexGenerators.VtxSmearedRealistic25ns13TeVEarly2017Collision_cfi')
process.load('GeneratorInterface.Core.genFilterSummary_cff')
process.load('FastSimulation.Configuration.SimIdeal_cff')
process.load('FastSimulation.Configuration.Reconstruction_BefMix_cff')
process.load('Configuration.StandardSequences.DigiDMPreMix_cff')
process.load('SimGeneral.MixingModule.digi_MixPreMix_cfi')
process.load('Configuration.StandardSequences.DataMixerPreMix_cff')
process.load('Configuration.StandardSequences.SimL1EmulatorDM_cff')
process.load('Configuration.StandardSequences.DigiToRawDM_cff')
process.load('Configuration.StandardSequences.L1Reco_cff')
process.load('FastSimulation.Configuration.Reconstruction_AftMix_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(10)
)

# Input source
process.source = cms.Source("EmptySource")

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('Configuration/GenProduction/python/SUS-RunIIFall17FSPremix-00069-fragment.py nevts:1'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.AODSIMoutput = cms.OutputModule("PoolOutputModule",
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('generation_step')
    ),
    compressionAlgorithm = cms.untracked.string('LZMA'),
    compressionLevel = cms.untracked.int32(4),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('AODSIM'),
        filterName = cms.untracked.string('')
    ),
    eventAutoFlushCompressedSize = cms.untracked.int32(31457280),
    fileName = cms.untracked.string('file:SUS-RunIIFall17FSPremix-00069.root'),
    outputCommands = process.AODSIMEventContent.outputCommands
)

# Additional output definition

# Other statements
process.genstepfilter.triggerConditions=cms.vstring("generation_step")
process.mix.digitizers = cms.PSet(process.theDigitizersMixPreMix)
process.mixData.input.fileNames = cms.untracked.vstring([
'root://eoscms.cern.ch//eos/cms/store/mc/RunIIFall17FSPrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUMoriond17_94X_mc2017_realistic_v15-v1/20005/5610116F-3EFA-E811-BACE-FA163EC04576.root','root://eoscms.cern.ch//eos/cms/store/mc/RunIIFall17FSPrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUMoriond17_94X_mc2017_realistic_v15-v1/20005/E274537D-3EFA-E811-96B4-FA163EF59FA1.root','root://eoscms.cern.ch//eos/cms/store/mc/RunIIFall17FSPrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUMoriond17_94X_mc2017_realistic_v15-v1/20005/EC5F757F-3EFA-E811-ACAC-FA163E05FE96.root','root://eoscms.cern.ch//eos/cms/store/mc/RunIIFall17FSPrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUMoriond17_94X_mc2017_realistic_v15-v1/20005/2A64BB6A-3EFA-E811-812F-FA163E0BB3A6.root','root://eoscms.cern.ch//eos/cms/store/mc/RunIIFall17FSPrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUMoriond17_94X_mc2017_realistic_v15-v1/20005/02208878-3EFA-E811-9D1F-FA163ECFAB7F.root','root://eoscms.cern.ch//eos/cms/store/mc/RunIIFall17FSPrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUMoriond17_94X_mc2017_realistic_v15-v1/20005/DCBE057D-3EFA-E811-923B-FA163E376AE7.root','root://eoscms.cern.ch//eos/cms/store/mc/RunIIFall17FSPrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUMoriond17_94X_mc2017_realistic_v15-v1/20005/F0806465-3FFA-E811-AAFF-FA163EC124A9.root','root://eoscms.cern.ch//eos/cms/store/mc/RunIIFall17FSPrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUMoriond17_94X_mc2017_realistic_v15-v1/20005/B4465B7C-3EFA-E811-B1B1-FA163E34467F.root','root://eoscms.cern.ch//eos/cms/store/mc/RunIIFall17FSPrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUMoriond17_94X_mc2017_realistic_v15-v1/20005/F0BB1A75-3EFA-E811-B9D4-FA163E26BC93.root','root://eoscms.cern.ch//eos/cms/store/mc/RunIIFall17FSPrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUMoriond17_94X_mc2017_realistic_v15-v1/20005/7878F776-3EFA-E811-A771-FA163EF90889.root','root://eoscms.cern.ch//eos/cms/store/mc/RunIIFall17FSPrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUMoriond17_94X_mc2017_realistic_v15-v1/20005/20DF3273-3EFA-E811-9457-FA163E26BC93.root','root://eoscms.cern.ch//eos/cms/store/mc/RunIIFall17FSPrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUMoriond17_94X_mc2017_realistic_v15-v1/20005/CCF21B75-3EFA-E811-B49A-FA163EF90889.root','root://eoscms.cern.ch//eos/cms/store/mc/RunIIFall17FSPrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUMoriond17_94X_mc2017_realistic_v15-v1/20005/46473673-3EFA-E811-A767-FA163E26BC93.root','root://eoscms.cern.ch//eos/cms/store/mc/RunIIFall17FSPrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUMoriond17_94X_mc2017_realistic_v15-v1/20005/7E6F4874-3EFA-E811-88A9-FA163E26BC93.root','root://eoscms.cern.ch//eos/cms/store/mc/RunIIFall17FSPrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUMoriond17_94X_mc2017_realistic_v15-v1/20005/18D85D75-3EFA-E811-AE2A-FA163E3EE95B.root','root://eoscms.cern.ch//eos/cms/store/mc/RunIIFall17FSPrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUMoriond17_94X_mc2017_realistic_v15-v1/20005/5C07DC6F-3EFA-E811-B088-FA163EE43D91.root','root://eoscms.cern.ch//eos/cms/store/mc/RunIIFall17FSPrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUMoriond17_94X_mc2017_realistic_v15-v1/20005/B42C8977-3EFA-E811-BBD3-FA163EABEBF3.root','root://eoscms.cern.ch//eos/cms/store/mc/RunIIFall17FSPrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUMoriond17_94X_mc2017_realistic_v15-v1/20003/A83ADB9F-3AFA-E811-8532-FA163E3637B6.root','root://eoscms.cern.ch//eos/cms/store/mc/RunIIFall17FSPrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUMoriond17_94X_mc2017_realistic_v15-v1/20003/9CF665A1-3AFA-E811-8F14-02163E01A014.root','root://eoscms.cern.ch//eos/cms/store/mc/RunIIFall17FSPrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUMoriond17_94X_mc2017_realistic_v15-v1/20003/80CD63AC-3AFA-E811-BB84-FA163E8B9DC9.root','root://eoscms.cern.ch//eos/cms/store/mc/RunIIFall17FSPrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUMoriond17_94X_mc2017_realistic_v15-v1/20003/3A0FBFAF-3AFA-E811-BCA3-FA163E521E8E.root','root://eoscms.cern.ch//eos/cms/store/mc/RunIIFall17FSPrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUMoriond17_94X_mc2017_realistic_v15-v1/20003/C0005B9C-3AFA-E811-957C-FA163EDA0FB2.root','root://eoscms.cern.ch//eos/cms/store/mc/RunIIFall17FSPrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUMoriond17_94X_mc2017_realistic_v15-v1/20003/5E5B79AD-3AFA-E811-969C-FA163E66C5CD.root','root://eoscms.cern.ch//eos/cms/store/mc/RunIIFall17FSPrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUMoriond17_94X_mc2017_realistic_v15-v1/20003/70479EA3-3AFA-E811-B796-02163E019F42.root','root://eoscms.cern.ch//eos/cms/store/mc/RunIIFall17FSPrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUMoriond17_94X_mc2017_realistic_v15-v1/20003/C03CA7A0-3AFA-E811-9E1A-FA163E00751D.root','root://eoscms.cern.ch//eos/cms/store/mc/RunIIFall17FSPrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUMoriond17_94X_mc2017_realistic_v15-v1/20003/609082A4-3AFA-E811-9D41-FA163E82A06B.root','root://eoscms.cern.ch//eos/cms/store/mc/RunIIFall17FSPrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUMoriond17_94X_mc2017_realistic_v15-v1/20003/C450859B-3AFA-E811-8C71-FA163E88012B.root','root://eoscms.cern.ch//eos/cms/store/mc/RunIIFall17FSPrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUMoriond17_94X_mc2017_realistic_v15-v1/20003/D6EF8EB3-3AFA-E811-8B2C-02163E01A036.root','root://eoscms.cern.ch//eos/cms/store/mc/RunIIFall17FSPrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUMoriond17_94X_mc2017_realistic_v15-v1/20005/F8960B2C-40FA-E811-9F38-FA163E8257B8.root','root://eoscms.cern.ch//eos/cms/store/mc/RunIIFall17FSPrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUMoriond17_94X_mc2017_realistic_v15-v1/20005/AA792726-40FA-E811-B9D7-FA163ED05A75.root','root://eoscms.cern.ch//eos/cms/store/mc/RunIIFall17FSPrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUMoriond17_94X_mc2017_realistic_v15-v1/20005/32CBD025-40FA-E811-B9B4-FA163E4200C7.root','root://eoscms.cern.ch//eos/cms/store/mc/RunIIFall17FSPrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUMoriond17_94X_mc2017_realistic_v15-v1/20005/4893D72C-40FA-E811-99CC-FA163EE83C78.root','root://eoscms.cern.ch//eos/cms/store/mc/RunIIFall17FSPrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUMoriond17_94X_mc2017_realistic_v15-v1/20005/044BF126-40FA-E811-9741-FA163ECB9FF9.root','root://eoscms.cern.ch//eos/cms/store/mc/RunIIFall17FSPrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUMoriond17_94X_mc2017_realistic_v15-v1/20005/BA3A292B-40FA-E811-A30A-02163E019FF2.root','root://eoscms.cern.ch//eos/cms/store/mc/RunIIFall17FSPrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUMoriond17_94X_mc2017_realistic_v15-v1/20005/7EB8DD25-40FA-E811-8483-FA163E92E6EA.root','root://eoscms.cern.ch//eos/cms/store/mc/RunIIFall17FSPrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUMoriond17_94X_mc2017_realistic_v15-v1/20005/EC786632-40FA-E811-AF3E-FA163E3DF9DF.root','root://eoscms.cern.ch//eos/cms/store/mc/RunIIFall17FSPrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUMoriond17_94X_mc2017_realistic_v15-v1/20005/BC124120-40FA-E811-98A7-FA163EBB779E.root','root://eoscms.cern.ch//eos/cms/store/mc/RunIIFall17FSPrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUMoriond17_94X_mc2017_realistic_v15-v1/20005/7469D33D-40FA-E811-A5E3-FA163E667536.root','root://eoscms.cern.ch//eos/cms/store/mc/RunIIFall17FSPrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUMoriond17_94X_mc2017_realistic_v15-v1/20005/C2DA4D22-40FA-E811-B1AF-FA163E3D2069.root','root://eoscms.cern.ch//eos/cms/store/mc/RunIIFall17FSPrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUMoriond17_94X_mc2017_realistic_v15-v1/20005/14759D2C-40FA-E811-82BF-FA163E6011FE.root','root://eoscms.cern.ch//eos/cms/store/mc/RunIIFall17FSPrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUMoriond17_94X_mc2017_realistic_v15-v1/20005/6C3C6E23-40FA-E811-AB16-FA163EDDE562.root','root://eoscms.cern.ch//eos/cms/store/mc/RunIIFall17FSPrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUMoriond17_94X_mc2017_realistic_v15-v1/20005/AC4AA737-40FA-E811-8EA5-FA163ED90FF1.root','root://eoscms.cern.ch//eos/cms/store/mc/RunIIFall17FSPrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUMoriond17_94X_mc2017_realistic_v15-v1/20005/6694DB36-40FA-E811-9914-FA163EFCCBD6.root','root://eoscms.cern.ch//eos/cms/store/mc/RunIIFall17FSPrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUMoriond17_94X_mc2017_realistic_v15-v1/20005/56FFAB38-40FA-E811-9C0C-FA163E2F2008.root','root://eoscms.cern.ch//eos/cms/store/mc/RunIIFall17FSPrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUMoriond17_94X_mc2017_realistic_v15-v1/20005/B4AE892A-40FA-E811-8DCC-FA163E2B710A.root','root://eoscms.cern.ch//eos/cms/store/mc/RunIIFall17FSPrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUMoriond17_94X_mc2017_realistic_v15-v1/20005/14EA7F3E-40FA-E811-9734-02163E01A066.root','root://eoscms.cern.ch//eos/cms/store/mc/RunIIFall17FSPrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUMoriond17_94X_mc2017_realistic_v15-v1/20005/70DB4F26-40FA-E811-92FC-FA163E2CEAC7.root','root://eoscms.cern.ch//eos/cms/store/mc/RunIIFall17FSPrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUMoriond17_94X_mc2017_realistic_v15-v1/20005/708FCB2D-40FA-E811-9104-02163E019FF1.root','root://eoscms.cern.ch//eos/cms/store/mc/RunIIFall17FSPrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUMoriond17_94X_mc2017_realistic_v15-v1/20005/B656664E-40FA-E811-BBF9-FA163ECDE73F.root','root://eoscms.cern.ch//eos/cms/store/mc/RunIIFall17FSPrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUMoriond17_94X_mc2017_realistic_v15-v1/20005/7065B579-3EFA-E811-AFE4-FA163E0BC49B.root','root://eoscms.cern.ch//eos/cms/store/mc/RunIIFall17FSPrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUMoriond17_94X_mc2017_realistic_v15-v1/20005/44AEE081-3EFA-E811-877B-FA163EA37B5E.root','root://eoscms.cern.ch//eos/cms/store/mc/RunIIFall17FSPrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUMoriond17_94X_mc2017_realistic_v15-v1/20005/82CC04B6-3EFA-E811-9D78-FA163ECFC1B3.root','root://eoscms.cern.ch//eos/cms/store/mc/RunIIFall17FSPrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUMoriond17_94X_mc2017_realistic_v15-v1/20005/22602571-3EFA-E811-86FD-FA163E6A6DD4.root','root://eoscms.cern.ch//eos/cms/store/mc/RunIIFall17FSPrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUMoriond17_94X_mc2017_realistic_v15-v1/20005/12089766-3FFA-E811-8698-FA163E6A6DD4.root','root://eoscms.cern.ch//eos/cms/store/mc/RunIIFall17FSPrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUMoriond17_94X_mc2017_realistic_v15-v1/20005/8EB77D72-3FFA-E811-AFE4-FA163E2B2370.root','root://eoscms.cern.ch//eos/cms/store/mc/RunIIFall17FSPrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUMoriond17_94X_mc2017_realistic_v15-v1/20005/D41E5651-3FFA-E811-A40B-FA163E968D2C.root','root://eoscms.cern.ch//eos/cms/store/mc/RunIIFall17FSPrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUMoriond17_94X_mc2017_realistic_v15-v1/10002/6094E83E-54FA-E811-9B66-FA163E5158D3.root','root://eoscms.cern.ch//eos/cms/store/mc/RunIIFall17FSPrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUMoriond17_94X_mc2017_realistic_v15-v1/10002/A869CAF8-54FA-E811-B428-FA163EB3FDE2.root','root://eoscms.cern.ch//eos/cms/store/mc/RunIIFall17FSPrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUMoriond17_94X_mc2017_realistic_v15-v1/10002/9A1177EE-54FA-E811-995D-FA163E8BEA21.root','root://eoscms.cern.ch//eos/cms/store/mc/RunIIFall17FSPrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUMoriond17_94X_mc2017_realistic_v15-v1/10002/806BADF0-54FA-E811-B356-FA163EEED0C0.root','root://eoscms.cern.ch//eos/cms/store/mc/RunIIFall17FSPrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUMoriond17_94X_mc2017_realistic_v15-v1/10002/00460B79-55FA-E811-AFCC-FA163EBFA897.root','root://eoscms.cern.ch//eos/cms/store/mc/RunIIFall17FSPrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUMoriond17_94X_mc2017_realistic_v15-v1/10002/8C52C8F1-54FA-E811-946B-FA163EA06145.root','root://eoscms.cern.ch//eos/cms/store/mc/RunIIFall17FSPrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUMoriond17_94X_mc2017_realistic_v15-v1/10002/FE8AD038-56FA-E811-B8F7-FA163E16328F.root','root://eoscms.cern.ch//eos/cms/store/mc/RunIIFall17FSPrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUMoriond17_94X_mc2017_realistic_v15-v1/10002/E6501A4B-56FA-E811-BFFB-FA163E9EB433.root','root://eoscms.cern.ch//eos/cms/store/mc/RunIIFall17FSPrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUMoriond17_94X_mc2017_realistic_v15-v1/10002/6C3DDB4E-56FA-E811-BAEB-FA163E91BB19.root','root://eoscms.cern.ch//eos/cms/store/mc/RunIIFall17FSPrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUMoriond17_94X_mc2017_realistic_v15-v1/10002/D8577B4B-56FA-E811-A6D9-FA163E0A36DB.root','root://eoscms.cern.ch//eos/cms/store/mc/RunIIFall17FSPrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUMoriond17_94X_mc2017_realistic_v15-v1/10002/F233B369-55FA-E811-8343-FA163EF0BB6D.root','root://eoscms.cern.ch//eos/cms/store/mc/RunIIFall17FSPrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUMoriond17_94X_mc2017_realistic_v15-v1/10002/E206804C-56FA-E811-97A8-FA163EA87461.root','root://eoscms.cern.ch//eos/cms/store/mc/RunIIFall17FSPrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUMoriond17_94X_mc2017_realistic_v15-v1/10002/A6E9DCC9-57FA-E811-BD1C-FA163E90CD48.root','root://eoscms.cern.ch//eos/cms/store/mc/RunIIFall17FSPrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUMoriond17_94X_mc2017_realistic_v15-v1/10002/A8D980A8-56FA-E811-B4BB-FA163EF3792D.root','root://eoscms.cern.ch//eos/cms/store/mc/RunIIFall17FSPrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUMoriond17_94X_mc2017_realistic_v15-v1/10002/36E362E2-57FA-E811-94B8-FA163E3D171F.root','root://eoscms.cern.ch//eos/cms/store/mc/RunIIFall17FSPrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUMoriond17_94X_mc2017_realistic_v15-v1/10002/82E3F819-57FA-E811-84EC-FA163E9B4407.root','root://eoscms.cern.ch//eos/cms/store/mc/RunIIFall17FSPrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUMoriond17_94X_mc2017_realistic_v15-v1/10002/D4EFABE4-57FA-E811-B022-FA163E9EB433.root','root://eoscms.cern.ch//eos/cms/store/mc/RunIIFall17FSPrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUMoriond17_94X_mc2017_realistic_v15-v1/10002/865A8AF1-54FA-E811-9666-FA163EA06145.root','root://eoscms.cern.ch//eos/cms/store/mc/RunIIFall17FSPrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUMoriond17_94X_mc2017_realistic_v15-v1/10002/9CE14D40-55FA-E811-B3AC-FA163E58A531.root','root://eoscms.cern.ch//eos/cms/store/mc/RunIIFall17FSPrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUMoriond17_94X_mc2017_realistic_v15-v1/10002/B8BA2AF6-54FA-E811-86F8-FA163E48A86B.root','root://eoscms.cern.ch//eos/cms/store/mc/RunIIFall17FSPrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUMoriond17_94X_mc2017_realistic_v15-v1/10002/3A86E779-5DFA-E811-96BF-FA163EEF00E2.root','root://eoscms.cern.ch//eos/cms/store/mc/RunIIFall17FSPrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUMoriond17_94X_mc2017_realistic_v15-v1/10000/A04C4451-43FA-E811-82DF-FA163E480AB4.root','root://eoscms.cern.ch//eos/cms/store/mc/RunIIFall17FSPrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUMoriond17_94X_mc2017_realistic_v15-v1/10000/6027D65B-43FA-E811-BEDC-FA163E3509C2.root','root://eoscms.cern.ch//eos/cms/store/mc/RunIIFall17FSPrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUMoriond17_94X_mc2017_realistic_v15-v1/10000/2EA5A366-42FA-E811-A504-FA163EA7BFB3.root','root://eoscms.cern.ch//eos/cms/store/mc/RunIIFall17FSPrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUMoriond17_94X_mc2017_realistic_v15-v1/10000/8E748E55-43FA-E811-9DA4-FA163EA7BFB3.root','root://eoscms.cern.ch//eos/cms/store/mc/RunIIFall17FSPrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUMoriond17_94X_mc2017_realistic_v15-v1/10004/18384A9D-60FA-E811-8AD5-FA163E02757D.root','root://eoscms.cern.ch//eos/cms/store/mc/RunIIFall17FSPrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUMoriond17_94X_mc2017_realistic_v15-v1/10004/B6A4A663-3DFA-E811-A95A-FA163E82A06B.root','root://eoscms.cern.ch//eos/cms/store/mc/RunIIFall17FSPrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUMoriond17_94X_mc2017_realistic_v15-v1/10000/3247315A-43FA-E811-93E4-FA163EB68402.root','root://eoscms.cern.ch//eos/cms/store/mc/RunIIFall17FSPrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUMoriond17_94X_mc2017_realistic_v15-v1/10003/B8C36EE8-60FA-E811-8022-FA163E76C639.root','root://eoscms.cern.ch//eos/cms/store/mc/RunIIFall17FSPrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUMoriond17_94X_mc2017_realistic_v15-v1/10003/20EABCED-60FA-E811-AA21-FA163E6FE97F.root','root://eoscms.cern.ch//eos/cms/store/mc/RunIIFall17FSPrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUMoriond17_94X_mc2017_realistic_v15-v1/10003/8E94F1EB-60FA-E811-A99B-FA163E6FE97F.root','root://eoscms.cern.ch//eos/cms/store/mc/RunIIFall17FSPrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUMoriond17_94X_mc2017_realistic_v15-v1/10003/1AE267BD-62FA-E811-93DA-FA163E126D94.root','root://eoscms.cern.ch//eos/cms/store/mc/RunIIFall17FSPrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUMoriond17_94X_mc2017_realistic_v15-v1/10003/04F269BC-62FA-E811-8DF4-FA163E126D94.root','root://eoscms.cern.ch//eos/cms/store/mc/RunIIFall17FSPrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUMoriond17_94X_mc2017_realistic_v15-v1/10002/A259B998-59FA-E811-B91A-FA163EBDEE56.root','root://eoscms.cern.ch//eos/cms/store/mc/RunIIFall17FSPrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUMoriond17_94X_mc2017_realistic_v15-v1/10002/8A0E0646-59FA-E811-A888-FA163E9F9831.root','root://eoscms.cern.ch//eos/cms/store/mc/RunIIFall17FSPrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUMoriond17_94X_mc2017_realistic_v15-v1/10002/60BE8248-59FA-E811-8B6B-FA163EB8E001.root','root://eoscms.cern.ch//eos/cms/store/mc/RunIIFall17FSPrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUMoriond17_94X_mc2017_realistic_v15-v1/10002/A26F2007-5AFA-E811-9BCA-FA163E36C3CA.root','root://eoscms.cern.ch//eos/cms/store/mc/RunIIFall17FSPrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUMoriond17_94X_mc2017_realistic_v15-v1/10002/806C4606-5AFA-E811-967B-FA163E17B0F8.root','root://eoscms.cern.ch//eos/cms/store/mc/RunIIFall17FSPrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUMoriond17_94X_mc2017_realistic_v15-v1/10002/5EF01700-5AFA-E811-A240-FA163E36C7EE.root','root://eoscms.cern.ch//eos/cms/store/mc/RunIIFall17FSPrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUMoriond17_94X_mc2017_realistic_v15-v1/10002/60B97B1C-5AFA-E811-B767-FA163EE3B4CD.root','root://eoscms.cern.ch//eos/cms/store/mc/RunIIFall17FSPrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUMoriond17_94X_mc2017_realistic_v15-v1/10002/B410871E-5BFA-E811-9300-FA163E43A3EC.root','root://eoscms.cern.ch//eos/cms/store/mc/RunIIFall17FSPrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUMoriond17_94X_mc2017_realistic_v15-v1/10002/7CAC542F-5AFA-E811-9E5E-FA163E830A80.root','root://eoscms.cern.ch//eos/cms/store/mc/RunIIFall17FSPrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUMoriond17_94X_mc2017_realistic_v15-v1/10002/CA48D302-5AFA-E811-8F8E-FA163E380296.root','root://eoscms.cern.ch//eos/cms/store/mc/RunIIFall17FSPrePremix/Neutrino_E-10_gun/GEN-SIM-DIGI-RAW/PUMoriond17_94X_mc2017_realistic_v15-v1/10002/FA868717-5AFA-E811-9CD1-FA163E10450E.root'
])
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '94X_mc2017_realistic_v15', '')

process.generator = cms.EDFilter("Pythia8GeneratorFilter",
    RandomizedParameters = cms.VPSet(cms.PSet(
        ConfigDescription = cms.string('T5WgStealth_1000_500'),
        ConfigWeight = cms.double(170.425531915),
        GridpackPath = cms.string('/cvmfs/cms.cern.ch/phys_generator/gridpacks/2017/13TeV/madgraph/V5_2.4.2/sus_sms/LO_PDF/SMS-GlGl/v1/SMS-GlGl_mGl-1000_slc6_amd64_gcc481_CMSSW_7_1_30_tarball.tar.xz'),
        PythiaParameters = cms.PSet(
            JetMatchingParameters = cms.vstring('JetMatching:setMad = off', 
                'JetMatching:scheme = 1', 
                'JetMatching:merge = on', 
                'JetMatching:jetAlgorithm = 2', 
                'JetMatching:etaJetMax = 5.', 
                'JetMatching:coneRadius = 1.', 
                'JetMatching:slowJetPower = 1', 
                'JetMatching:qCut = 140', 
                'JetMatching:nQmatch = 5', 
                'JetMatching:nJetMax = 2', 
                'JetMatching:doShowerKt = off', 
                '6:m0 = 172.5', 
                '24:mMin = 0.1', 
                'Check:abortIfVeto = on'),
            parameterSets = cms.vstring('pythia8CommonSettings', 
                'pythia8CP2Settings', 
                'JetMatchingParameters'),
            pythia8CP2Settings = cms.vstring('Tune:pp 14', 
                'Tune:ee 7', 
                'MultipartonInteractions:ecmPow=0.1391', 
                'PDF:pSet=17', 
                'MultipartonInteractions:bProfile=2', 
                'MultipartonInteractions:pT0Ref=2.306', 
                'MultipartonInteractions:coreRadius=0.3755', 
                'MultipartonInteractions:coreFraction=0.3269', 
                'ColourReconnection:range=2.323', 
                'SigmaTotal:zeroAXB=off', 
                'SpaceShower:rapidityOrder=off', 
                'SpaceShower:alphaSvalue=0.13', 
                'TimeShower:alphaSvalue=0.13'),
            pythia8CommonSettings = cms.vstring('Tune:preferLHAPDF = 2', 
                'Main:timesAllowErrors = 10000', 
                'Check:epTolErr = 0.01', 
                'Beams:setProductionScalesFromLHEF = off', 
                'SLHA:keepSM = on', 
                'SLHA:minMassSM = 1000.', 
                'ParticleDecays:limitTau0 = on', 
                'ParticleDecays:tau0Max = 10', 
                'ParticleDecays:allowPhotonRadiation = on')
        ),
        SLHATableForPythia8 = cms.string('\nBLOCK MODSEL  # Model selection\n    1     1   sugra\n#\nBLOCK QNUMBERS 3000001 # f\n    1  0 # 3 times electric charge\n    2  2 # number of spin states (2S+1)\n    3  1 # colour rep (1: singlet, 3: triplet, 8: octet)\n    4  0 # Particle/Antiparticle distinction (0=own anti)\n#\nBLOCK QNUMBERS 3000002 # n\n    1  0 # 3 times electric charge\n    2  1 # number of spin states (2S+1)\n    3  1 # colour rep (1: singlet, 3: triplet, 8: octet)\n    4  0 # Particle/Antiparticle distinction (0=own anti)\nBLOCK MASS\n   2000001     1.00000000E+10\n   2000002     1.00000000E+10\n   2000003     1.00000000E+10\n   2000004     1.00000000E+10\n   2000005     1.00000000E+10\n   2000006     1.00000000E+10\n   2000011     1.00000000E+10\n   2000013     1.00000000E+10\n   2000015     1.00000000E+10\n   1000001     1.00000000E+10\n   1000002     1.00000000E+10\n   1000003     1.00000000E+10\n   1000004     1.00000000E+10\n   1000005     1.00000000E+10\n   1000006     1.00000000E+10\n   1000011     1.00000000E+10\n   1000012     1.00000000E+10\n   1000013     1.00000000E+10\n   1000014     1.00000000E+10\n   1000015     1.00000000E+10\n   1000016     1.00000000E+10\n   1000021     1.000000e+03\n   1000022     5.000000e+02\n   1000023     1.00000000E+10\n   1000024     5.000000e+02\n   1000025     1.00000000E+10\n   1000035     1.00000000E+10\n   1000037     1.00000000E+10\n   1000039                0.0   #  Gravitino\n   3000001     1.00000000E+02   #  f: stealth sector\n   3000002     9.00000000E+01   #  n: stealth sector\n#\nDECAY   2000001     0.00000000E+00\nDECAY   2000002     0.00000000E+00\nDECAY   2000003     0.00000000E+00\nDECAY   2000004     0.00000000E+00\nDECAY   2000005     0.00000000E+00\nDECAY   2000006     0.00000000E+00\nDECAY   2000011     0.00000000E+00\nDECAY   2000013     0.00000000E+00\nDECAY   2000015     0.00000000E+00\nDECAY   1000001     0.00000000E+00\nDECAY   1000002     0.00000000E+00\nDECAY   1000003     0.00000000E+00\nDECAY   1000004     0.00000000E+00\nDECAY   1000005     0.00000000E+00\nDECAY   1000006     0.00000000E+00\nDECAY   1000011     0.00000000E+00\nDECAY   1000012     0.00000000E+00\nDECAY   1000013     0.00000000E+00\nDECAY   1000014     0.00000000E+00\nDECAY   1000015     0.00000000E+00\nDECAY   1000016     0.00000000E+00\n\nDECAY   1000021     1.00000000E+00\n     0.00000000E+00    3         -6          6    1000022\n     1.00000000E-01    3         -1          1    1000022\n     1.00000000E-01    3         -2          2    1000022\n     1.00000000E-01    3         -3          3    1000022\n     1.00000000E-01    3         -4          4    1000022\n     1.00000000E-01    3         -5          5    1000022\n     1.25000000E-01    3         -2          1    1000024\n     1.25000000E-01    3          2         -1    -1000024\n     1.25000000E-01    3         -4          3    1000024\n     1.25000000E-01    3          4         -3    -1000024\n\nDECAY   1000022     1.00000000E-03\n     0.0000000    2     3000001        22\n     1.0000000    2     3000001        22\nDECAY   1000024     1.00000000E-03\n     0.0000000    3     3000001        -1      2\n     1.0000000    2     3000001        24\n\nDECAY   3000001   1.00000000E-06   # f decays\n     1.00000000e+00    2     1000039   3000002   # BR(f -> gs n )\nDECAY   3000002   1.00000000E-06   # n decays\n     1.00000000e+00    2          21        21   # BR(n -> g g )\n\nDECAY   1000039     0.00000000E+00\n')
    )),
    comEnergy = cms.double(13000.0),
    filterEfficiency = cms.untracked.double(1.0),
    maxEventsToPrint = cms.untracked.int32(1),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    pythiaPylistVerbosity = cms.untracked.int32(1)
)


# Path and EndPath definitions
process.generation_step = cms.Path(process.pgen)
process.simulation_step = cms.Path(process.psim)
process.reconstruction_befmix_step = cms.Path(process.reconstruction_befmix)
process.digitisation_step = cms.Path(process.pdigi)
process.datamixing_step = cms.Path(process.pdatamix)
process.L1simulation_step = cms.Path(process.SimL1Emulator)
process.digi2raw_step = cms.Path(process.DigiToRaw)
process.L1Reco_step = cms.Path(process.L1Reco)
process.reconstruction_step = cms.Path(process.reconstruction)
process.genfiltersummary_step = cms.EndPath(process.genFilterSummary)
process.endjob_step = cms.EndPath(process.endOfProcess)
process.AODSIMoutput_step = cms.EndPath(process.AODSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.generation_step,process.genfiltersummary_step,process.simulation_step,process.reconstruction_befmix_step,process.digitisation_step,process.datamixing_step,process.L1simulation_step,process.digi2raw_step,process.L1Reco_step,process.reconstruction_step,process.endjob_step,process.AODSIMoutput_step)
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)
# filter all path with the production filter sequence
for path in process.paths:
	getattr(process,path)._seq = process.generator * getattr(process,path)._seq 


# Customisation from command line

process.source.numberEventsInLuminosityBlock = cms.untracked.uint32(200)
#Have logErrorHarvester wait for the same EDProducers to finish as those providing data for the OutputModule
from FWCore.Modules.logErrorHarvester_cff import customiseLogErrorHarvesterUsingOutputCommands
process = customiseLogErrorHarvesterUsingOutputCommands(process)

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion
