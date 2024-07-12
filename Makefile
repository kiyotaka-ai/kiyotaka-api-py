PROTO_DIR := ./proto
DIST := ./tharamine

IMPORTS := -I $(PROTO_DIR)/service/ -I $(PROTO_DIR)/lib/ -I $(PROTO_DIR)/types/
FILES := $(PROTO_DIR)/service/api/*.proto \
		$(PROTO_DIR)/lib/timestamp/timestamp.proto \
		$(PROTO_DIR)/types/trade.proto \
		$(PROTO_DIR)/types/trade_aggregation.proto \
		$(PROTO_DIR)/types/trade_side_agnostic_aggregation.proto

.PHONY: all clean

all: $(DIST)

$(DIST):
	mkdir -p $(DIST)
	protoc $(IMPORTS) \
		--python_betterproto_out=$(DIST) \
		$(FILES)

clean:
	rm -rf $(DIST)
