PNP4NAGIOS := pnp4nagios

PNP4NAGIOS_BUILD := $(BUILD_HELPER_DIR)/$(PNP4NAGIOS)-build
PNP4NAGIOS_INSTALL := $(BUILD_HELPER_DIR)/$(PNP4NAGIOS)-install

# Unset CONFIG_SITE
CONFIG_SITE = ''

$(PNP4NAGIOS_BUILD):
	$(BAZEL_BUILD) @pnp4nagios//:pnp4nagios
	$(BAZEL_BUILD) @pnp4nagios//:skel

$(PNP4NAGIOS_INSTALL): $(PNP4NAGIOS_BUILD)
	$(RSYNC) --chmod=u+w $(BAZEL_BIN)/$(PNP4NAGIOS)/$(PNP4NAGIOS)/ $(DESTDIR)$(OMD_ROOT)/
	$(RSYNC) --chmod=u+w $(BAZEL_BIN)/$(PNP4NAGIOS)/skel/ $(DESTDIR)$(OMD_ROOT)/skel
	install -m 644 $(BAZEL_BIN)/$(PNP4NAGIOS)/share/diskspace/pnp4nagios $(DESTDIR)$(OMD_ROOT)/share/diskspace/pnp4nagios
	install -m 755 $(BAZEL_BIN)/$(PNP4NAGIOS)/lib/omd/hooks/PNP4NAGIOS $(DESTDIR)$(OMD_ROOT)/lib/omd/hooks/
	# Add symlinks, as bazel is dereferencing them
	cd $(DESTDIR)$(OMD_ROOT)/skel/etc/rc.d/ ; \
	ln -sf ../init.d/npcd 50-npcd ; \
	ln -sf ../init.d/pnp_gearman_worker 52-pnp_gearman_worker
