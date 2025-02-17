<!--
Copyright (C) 2024 Checkmk GmbH - License: GNU General Public License v2
This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
conditions defined in the file COPYING, which is part of this source code package.
-->
<script setup lang="ts">
import { CheckboxIndicator, CheckboxRoot } from 'radix-vue'
import checkboxChecked from '@/assets/checkbox-x.svg'
import CmkSpace from '@/components/CmkSpace.vue'
const value = defineModel<boolean>({ required: false, default: false })

interface CmkCheckboxProps {
  label?: string
}

const props = defineProps<CmkCheckboxProps>()
</script>

<template>
  <label class="cmk-checkbox">
    <CheckboxRoot v-model:checked="value" class="cmk-checkbox__button">
      <CheckboxIndicator class="cmk-checkbox__indicator">
        <img :src="checkboxChecked" />
      </CheckboxIndicator>
    </CheckboxRoot>
    <span v-if="props.label"><CmkSpace size="small" />{{ label }}</span>
  </label>
</template>

<style scoped>
.cmk-checkbox {
  cursor: pointer;
  display: inline-block;
}
.cmk-checkbox :deep(.cmk-checkbox__button) {
  background-color: var(--default-form-element-bg-color);
  border: 1px solid var(--default-form-element-bg-color);
  border-radius: 2px;
  height: 12.5px;
  width: 12.5px;

  box-shadow: none; /* disable active/focus style of button */
  padding: 0;
  margin: 0;
  vertical-align: middle; /* otherwise will jump without cmk-frontend styles when checked/unchecked */
}
.cmk-checkbox:hover :deep(.cmk-checkbox__button) {
  background-color: var(--input-hover-bg-color);
}
.cmk-checkbox .cmk-checkbox__indicator {
  display: flex;
  justify-content: center;
  align-items: center;
}
.cmk-checkbox .cmk-checkbox__indicator img {
  width: 8px;
}
</style>
