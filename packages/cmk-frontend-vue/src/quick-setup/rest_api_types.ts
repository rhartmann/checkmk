/**
 * Copyright (C) 2024 Checkmk GmbH - License: GNU General Public License v2
 * This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
 * conditions defined in the file COPYING, which is part of this source code package.
 */
import { type ComponentSpec } from '@/quick-setup/components/quick-setup/widgets/widget_types'
import type { ValidationMessages } from '@/form'

/**
 * Common stage structure
 */
export interface QSStageStructure {
  components: ComponentSpec[]
  load_wait_label: string
  next_button?: QSStageButton
  prev_button?: QSStageButton
}

/**
 * Regular buttons
 */
export interface QSStageButton {
  label: string
  aria_label?: string | null
}

/**
 * Save button
 */
export interface QSCompleteButton {
  id: string
  label: string
  ariaLabel?: string | null
}

interface QSCommonInitializationResponse {
  quick_setup_id: string
  guided_mode_string: string
  overview_mode_string: string
  complete_buttons: QSCompleteButton[]

  /** previous stage button for save stage */
  prev_button: QSStageButton
}

/**
 * Response from the API when initializing the quick setup when in guided mode
 */
export interface QSInitializationResponse extends QSCommonInitializationResponse {
  overviews: QSOverviewSpec[]
  stage: {
    stage_id: number
    stage_recap: ComponentSpec[]
    next_stage_structure: QSStageStructure
  }
}

interface QSStage extends QSOverviewSpec, QSStageStructure {}

/**
 * Response from the API when initializing the quick setup when in overview mode
 */
export interface QSAllStagesResponse extends QSCommonInitializationResponse {
  stages: QSStage[]
}

/**
 * Overview spec (QuickSetupStageOverviewResponse)
 */
export interface QSOverviewSpec {
  title: string
  sub_title: string | null
}

/**
 * Request for stage validation (QuickSetupStageRequest)
 */
interface QSStageRequest {
  form_data: object
}

/**
 * Request to validate the current stage (QuickSetupRequest)
 */
export interface QSValidateStagesRequest {
  quick_setup_id: string
  stages: QSStageRequest[]
}

/**
 * Response from the API when validating a stage (QuickSetupStageResponse)
 */
export interface QSStageResponse {
  stage_recap: ComponentSpec[]
  next_stage_structure: QSStageStructure
  errors: QsStageValidationError | null
}

/**
 * Error types from stage validation
 */
export interface QsStageValidationError {
  formspec_errors: Record<string, ValidationMessages>
  stage_errors: string[]
}

export interface RestApiError {
  type: string
}

export interface ValidationError extends RestApiError, QsStageValidationError {
  type: 'validation'
}
export interface GeneralError extends RestApiError {
  type: 'general'
  general_error: string
}

/**
 * Request to complete the quick setup (QuickSetupFinalSaveRequest)
 */
export interface QSRequestComplete {
  button_id: string
  stages: QSStageRequest[]
}

export interface QSResponseComplete {
  redirect_url: string
}
