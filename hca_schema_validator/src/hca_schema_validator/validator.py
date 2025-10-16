"""HCA Validator - extends cellxgene Validator with HCA-specific rules."""

import os
import yaml

from cellxgene_schema.validate import Validator
from . import __schema_version__ as HCA_SCHEMA_VERSION


class HCAValidator(Validator):
    """
    HCA-specific validator extending cellxgene schema validation.
    
    Uses a custom schema definition that differs from CELLxGENE in key areas:
    - organism and organism_ontology_term_id are in obs (not uns)
    """
    
    def __init__(self, ignore_labels=False):
        """
        Initialize HCA validator.
        
        Args:
            ignore_labels: If True, skip label validation
        """
        super().__init__(ignore_labels=ignore_labels)
    
    def _set_schema_def(self):
        """
        Sets schema dictionary using HCA-specific schema definition.
        
        Overrides the base method to load HCA's custom schema instead of
        the default CELLxGENE schema.
        """
        if not self.schema_version:
            # Use HCA schema version
            self.schema_version = HCA_SCHEMA_VERSION
        
        if not self.schema_def:
            # Load HCA-specific schema
            package_root = os.path.dirname(os.path.realpath(__file__))
            schema_path = os.path.join(
                package_root, 
                "schema_definitions", 
                "hca_schema_definition.yaml"
            )
            
            with open(schema_path) as fp:
                self.schema_def = yaml.load(fp, Loader=yaml.FullLoader)
