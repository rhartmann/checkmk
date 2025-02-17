#!/usr/bin/env python3
# Copyright (C) 2019 Checkmk GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.

"""Central module for common (non-edition specific) registrations"""

from cmk.ccc.crash_reporting import crash_report_registry
from cmk.ccc.version import edition

from cmk.utils import paths
from cmk.utils.licensing.registry import register_cre_licensing_handler

import cmk.gui.help
from cmk.gui import (
    agent_registration,
    autocompleters,
    crash_handler,
    crash_reporting,
    default_permissions,
    graphing,
    gui_background_job,
    help_menu,
    inventory,
    login,
    logwatch,
    main,
    message,
    mobile,
    notifications,
    pagetypes,
    painter_options,
    piggyback_hub,
    prediction,
    user_message,
    valuespec,
    weblib,
    werks,
)
from cmk.gui.background_job import job_registry
from cmk.gui.background_job import registration as background_job_registration
from cmk.gui.bi import registration as bi_registration
from cmk.gui.config import register_post_config_load_hook
from cmk.gui.dashboard import dashlet_registry
from cmk.gui.dashboard import registration as dashboard_registration
from cmk.gui.data_source import data_source_registry
from cmk.gui.main_menu import mega_menu_registry
from cmk.gui.nodevis import nodevis
from cmk.gui.openapi import endpoint_registry
from cmk.gui.openapi import registration as openapi_registration
from cmk.gui.pages import page_registry
from cmk.gui.painter.v0.base import painter_registry
from cmk.gui.painter_options import painter_option_registry
from cmk.gui.permissions import permission_registry, permission_section_registry
from cmk.gui.quick_setup import registration as quick_setup_registration
from cmk.gui.quick_setup.v0_unstable._registry import quick_setup_registry
from cmk.gui.sidebar import snapin_registry
from cmk.gui.userdb import register_config_file as user_connections_config
from cmk.gui.userdb import register_userroles_config_file as register_userroles
from cmk.gui.userdb import registration as userdb_registration
from cmk.gui.userdb import user_attribute_registry, user_connector_registry
from cmk.gui.valuespec import autocompleter_registry
from cmk.gui.views import registration as views_registration
from cmk.gui.views.command import command_group_registry, command_registry
from cmk.gui.views.icon import icon_and_action_registry
from cmk.gui.views.layout import layout_registry
from cmk.gui.views.row_post_processing import row_post_processor_registry
from cmk.gui.views.sorter import sorter_registry
from cmk.gui.views.store import multisite_builtin_views
from cmk.gui.visuals.filter import filter_registry
from cmk.gui.visuals.info import visual_info_registry
from cmk.gui.visuals.type import visual_type_registry
from cmk.gui.watolib import broker_connections as broker_connections_config
from cmk.gui.watolib import configuration_bundles, groups_io, password_store
from cmk.gui.watolib import notifications as notifications_config
from cmk.gui.watolib import registration as watolib_registration
from cmk.gui.watolib import rulesets as rule_config
from cmk.gui.watolib import sites as sites_config
from cmk.gui.watolib import tags as tag_config
from cmk.gui.watolib import users as user_config
from cmk.gui.watolib.automation_commands import automation_command_registry
from cmk.gui.watolib.config_domain_name import (
    config_domain_registry,
    config_variable_group_registry,
    config_variable_registry,
    sample_config_generator_registry,
)
from cmk.gui.watolib.config_sync import replication_path_registry
from cmk.gui.watolib.groups import contact_group_usage_finder_registry
from cmk.gui.watolib.host_attributes import host_attribute_registry, host_attribute_topic_registry
from cmk.gui.watolib.host_rename import rename_host_hook_registry
from cmk.gui.watolib.hosts_and_folders import folder_validators_registry
from cmk.gui.watolib.main_menu import main_module_registry, main_module_topic_registry
from cmk.gui.watolib.mode import mode_registry
from cmk.gui.watolib.rulespecs import rulespec_group_registry, rulespec_registry
from cmk.gui.watolib.search import match_item_generator_registry
from cmk.gui.watolib.simple_config_file import config_file_registry
from cmk.gui.watolib.timeperiods import timeperiod_usage_finder_registry


def register() -> None:
    pagetypes.register(mega_menu_registry)
    help_menu.register(mega_menu_registry)
    crash_handler.register(crash_report_registry)
    default_permissions.register(permission_section_registry, permission_registry)
    register_cre_licensing_handler()
    painter_options.register(painter_option_registry)
    views_registration.register(
        permission_section_registry,
        permission_registry,
        page_registry,
        visual_type_registry,
        register_post_config_load_hook,
        multisite_builtin_views,
        row_post_processor_registry,
    )
    inventory.register(
        page_registry,
        visual_info_registry,
        filter_registry,
        rulespec_group_registry,
        rulespec_registry,
        icon_and_action_registry,
    )
    dashboard_registration.register(
        permission_section_registry,
        page_registry,
        visual_type_registry,
        dashlet_registry,
        contact_group_usage_finder_registry,
        autocompleter_registry,
    )
    crash_reporting.register(
        page_registry,
        data_source_registry,
        painter_registry,
        sorter_registry,
        command_registry,
        config_variable_group_registry,
        config_variable_registry,
    )
    watolib_registration.register(
        edition(paths.omd_root),
        rulespec_group_registry,
        automation_command_registry,
        job_registry,
        sample_config_generator_registry,
        config_domain_registry,
        host_attribute_topic_registry,
        host_attribute_registry,
        contact_group_usage_finder_registry,
        timeperiod_usage_finder_registry,
        config_variable_group_registry,
        autocompleter_registry,
        match_item_generator_registry,
        replication_path_registry,
        folder_validators_registry,
    )
    piggyback_hub.register(
        config_domain_registry,
        config_variable_group_registry,
        config_variable_registry,
    )

    mobile.register(layout_registry)
    userdb_registration.register(
        page_registry,
        user_attribute_registry,
        user_connector_registry,
        job_registry,
        contact_group_usage_finder_registry,
        timeperiod_usage_finder_registry,
    )

    bi_registration.register(
        data_source_registry,
        painter_registry,
        painter_option_registry,
        permission_section_registry,
        permission_registry,
        page_registry,
        filter_registry,
        rename_host_hook_registry,
        main_module_topic_registry,
        main_module_registry,
        mode_registry,
        icon_and_action_registry,
        snapin_registry,
        endpoint_registry,
        command_registry,
        command_group_registry,
    )
    nodevis.register(page_registry, filter_registry, icon_and_action_registry)
    notifications.register(page_registry, permission_section_registry)
    user_message.register(page_registry)
    valuespec.register(page_registry)
    autocompleters.register(page_registry, autocompleter_registry)
    werks.register(page_registry)
    login.register(page_registry)
    message.register(page_registry)
    cmk.gui.help.register(page_registry)
    main.register(page_registry)
    logwatch.register(page_registry)
    prediction.register(page_registry)
    quick_setup_registration.register(main_module_registry, mode_registry, quick_setup_registry)
    background_job_registration.register(page_registry, mode_registry, main_module_registry)
    gui_background_job.register(permission_section_registry, permission_registry)
    graphing.register(page_registry, config_variable_registry, autocompleter_registry)
    agent_registration.register(permission_section_registry)
    weblib.register(page_registry)
    openapi_registration.register(endpoint_registry, job_registry)

    register_userroles(config_file_registry)
    groups_io.register(config_file_registry)
    password_store.register(config_file_registry)
    notifications_config.register(config_file_registry)
    tag_config.register(config_file_registry)
    sites_config.register(config_file_registry)
    broker_connections_config.register(config_file_registry)
    user_connections_config(config_file_registry)
    user_config.register(config_file_registry)
    rule_config.register(config_file_registry)
    configuration_bundles.register(config_file_registry)


register()
