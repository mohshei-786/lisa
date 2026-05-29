# Copyright (c) Microsoft Corporation.
# Licensed under the MIT license.
"""
Pluggy hookspecs for the BMI platform.

Mirrors ``lisa.sut_orchestrator.azure.hooks`` so out-of-tree extensions can
mutate the loaded BMI ARM template (e.g. inject NSG rules) before deployment.
"""

from typing import Any, Dict, Optional

from lisa.environment import Environment
from lisa.util import hookspec, plugin_manager


class BmiHookSpec:
    @hookspec
    def bmi_update_arm_template(
        self,
        template: Dict[str, Any],
        parameters: Dict[str, Any],
        environment: Optional[Environment],
    ) -> None:
        """Mutate the BMI ARM template in-place before deployment.

        Args:
            template: dict loaded from ``autogen_bmi_template.json``.
            parameters: ARM deployment parameters
                ({paramName: {"value": ...}} pairs), readable by the hook
                to compute things like the NAT destination port range.
            environment: deploying LISA environment, or ``None`` when the
                deployer is invoked outside of an environment context.
        """
        ...


plugin_manager.add_hookspecs(BmiHookSpec)
